from datetime import datetime
from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user
from sqlalchemy import desc

from app import app, db
from forms import LoginForm, RegistrationForm
from models import ContenidoCosmico, ImagenCosmica, Usuario, VideoCosmico


@app.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = Usuario.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            user.ultimo_acceso = datetime.utcnow()
            db.session.commit()
            
            next_page = request.args.get('next')
            return redirect(next_page or url_for('dashboard'))
        else:
            flash('Nombre de usuario o contraseña incorrectos', 'error')
    
    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    
    form = RegistrationForm()
    if form.validate_on_submit():
        user = Usuario(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        
        db.session.add(user)
        db.session.commit()
        
        flash('¡Registro exitoso! Ahora puedes iniciar sesión.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Has cerrado sesión correctamente', 'info')
    return redirect(url_for('index'))


@app.route('/dashboard')
@login_required
def dashboard():
    contenidos = ContenidoCosmico.query.order_by(desc(ContenidoCosmico.fecha_creacion)).limit(3).all()
    videos = VideoCosmico.query.limit(2).all()
    imagenes = ImagenCosmica.query.limit(4).all()
    
    return render_template('dashboard.html', 
                          contenidos=contenidos, 
                          videos=videos, 
                          imagenes=imagenes)


@app.route('/big-bang')
@login_required
def big_bang():
    contenidos = ContenidoCosmico.query.filter_by(categoria='big_bang').all()
    videos = VideoCosmico.query.filter_by(categoria='big_bang').all()
    imagenes = ImagenCosmica.query.filter_by(categoria='big_bang').all()
    
    return render_template('big_bang.html', 
                          contenidos=contenidos, 
                          videos=videos, 
                          imagenes=imagenes)


@app.route('/theories')
@login_required
def theories():
    contenidos = ContenidoCosmico.query.filter_by(categoria='theories').all()
    videos = VideoCosmico.query.filter_by(categoria='theories').all()
    imagenes = ImagenCosmica.query.filter_by(categoria='theories').all()
    
    return render_template('theories.html', 
                          contenidos=contenidos, 
                          videos=videos, 
                          imagenes=imagenes)


@app.route('/philosophy')
@login_required
def philosophy():
    contenidos = ContenidoCosmico.query.filter_by(categoria='philosophy').all()
    videos = VideoCosmico.query.filter_by(categoria='philosophy').all()
    imagenes = ImagenCosmica.query.filter_by(categoria='philosophy').all()
    
    return render_template('philosophy.html', 
                          contenidos=contenidos, 
                          videos=videos, 
                          imagenes=imagenes)


@app.route('/space-time')
@login_required
def space_time():
    contenidos = ContenidoCosmico.query.filter_by(categoria='space_time').all()
    videos = VideoCosmico.query.filter_by(categoria='space_time').all()
    imagenes = ImagenCosmica.query.filter_by(categoria='space_time').all()
    
    return render_template('space_time.html', 
                          contenidos=contenidos, 
                          videos=videos, 
                          imagenes=imagenes)


@app.route('/gallery')
@login_required
def gallery():
    imagenes = ImagenCosmica.query.all()
    return render_template('gallery.html', imagenes=imagenes)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


# Initialize database with content
def initialize_db():
    # Crear usuario administrador predeterminado si no existe ningún usuario
    if Usuario.query.count() == 0:
        admin_user = Usuario(
            username="admin",
            email="admin@cosmicexplorer.com"
        )
        admin_user.set_password("admin12345")
        db.session.add(admin_user)
        db.session.commit()
        print("Usuario administrador creado - Usuario: admin, Contraseña: admin12345")
    
    # Only add content if tables are empty
    if ContenidoCosmico.query.count() == 0:
        # Add some basic content about the origin of the universe
        contenidos = [
            ContenidoCosmico(
                titulo="La Gran Explosión - El Inicio de Todo",
                contenido="""
                El Big Bang es la teoría cosmológica predominante sobre el origen y evolución del universo. 
                Según esta teoría, el universo comenzó en un estado extremadamente caliente y denso 
                hace aproximadamente 13.8 mil millones de años y se ha estado expandiendo desde entonces.
                
                Los científicos llegaron a esta teoría tras observar que las galaxias se están alejando 
                unas de otras, lo que sugiere que en el pasado todo estaba mucho más cercano.
                """,
                categoria="big_bang"
            ),
            ContenidoCosmico(
                titulo="La Expansión Cósmica",
                contenido="""
                Después del Big Bang, el universo se expandió a un ritmo extraordinario, un proceso 
                conocido como inflación cósmica. Durante esta fase, el universo se expandió exponencialmente, 
                allanando las irregularidades y estableciendo las condiciones para la formación de 
                galaxias y estrellas.
                
                La expansión continúa hoy en día, y los astrónomos han descubierto que incluso 
                se está acelerando, impulsada por una misteriosa fuerza llamada energía oscura.
                """,
                categoria="big_bang"
            ),
            ContenidoCosmico(
                titulo="Teoría de Cuerdas",
                contenido="""
                La teoría de cuerdas propone que las partículas fundamentales del universo no son 
                puntos, sino minúsculas cuerdas vibrantes. Dependiendo de cómo vibren estas cuerdas, 
                se manifiestan como diferentes partículas.
                
                Esta teoría intenta unificar la mecánica cuántica con la relatividad general, 
                los dos grandes pilares de la física moderna que han demostrado ser incompatibles 
                en situaciones extremas.
                """,
                categoria="theories"
            ),
            ContenidoCosmico(
                titulo="Multiverso y Universos Paralelos",
                contenido="""
                La teoría del multiverso sugiere que nuestro universo es solo uno de muchos universos 
                que existen en paralelo. Estos universos podrían tener diferentes leyes físicas, 
                constantes y dimensiones.
                
                Esta teoría surge de varias áreas de la física, incluyendo la teoría de cuerdas, 
                la inflación cósmica y la interpretación de muchos mundos de la mecánica cuántica.
                """,
                categoria="theories"
            ),
            ContenidoCosmico(
                titulo="Visiones Filosóficas Antiguas",
                contenido="""
                Muchas culturas antiguas tenían sus propias concepciones sobre el origen del universo. 
                Los griegos, como Aristóteles, creían en un universo eterno y sin cambios. En la cosmología 
                oriental, ciclos de creación y destrucción dominan la narrativa cósmica.
                
                Estas visiones filosóficas, aunque distintas de las teorías científicas modernas, 
                reflejan el esfuerzo humano por comprender nuestro lugar en el cosmos.
                """,
                categoria="philosophy"
            ),
            ContenidoCosmico(
                titulo="La Relatividad y la Naturaleza del Tiempo",
                contenido="""
                La teoría de la relatividad de Einstein revolucionó nuestra comprensión del espacio y el tiempo. 
                Según Einstein, el espacio y el tiempo no son entidades separadas sino un continuo 
                entrelazado llamado espacio-tiempo.
                
                Esta teoría predice fenómenos asombrosos como la dilatación del tiempo, donde el tiempo 
                fluye más lentamente en campos gravitacionales fuertes o a velocidades cercanas a la luz.
                """,
                categoria="space_time"
            ),
            ContenidoCosmico(
                titulo="Agujeros Negros: Los Devoradores Cósmicos",
                contenido="""
                Los agujeros negros son regiones del espacio-tiempo donde la gravedad es tan intensa 
                que nada, ni siquiera la luz, puede escapar una vez que cruza el horizonte de eventos.
                
                Estos objetos astronómicos fascinantes nacen cuando estrellas masivas colapsan bajo su 
                propia gravedad. Los agujeros negros supermasivos habitan en el centro de la mayoría 
                de las galaxias, incluida nuestra Vía Láctea.
                """,
                categoria="space_time"
            )
        ]
        db.session.add_all(contenidos)
        
        # Add videos about the universe
        videos = [
            VideoCosmico(
                titulo="El Origen del Universo: El Big Bang",
                descripcion="Documental que explica detalladamente la teoría del Big Bang y cómo comenzó nuestro universo.",
                youtube_id="7pL5vzIMAhs",
                categoria="big_bang"
            ),
            VideoCosmico(
                titulo="¿Qué Existía Antes del Big Bang?",
                descripcion="Una exploración de las teorías científicas que intentan explicar qué podría haber existido antes del inicio del universo.",
                youtube_id="BOLHtIvEX58",
                categoria="big_bang"
            ),
            VideoCosmico(
                titulo="La Teoría de Cuerdas Explicada",
                descripcion="Explicación detallada de cómo la teoría de cuerdas intenta unificar las fuerzas fundamentales del universo.",
                youtube_id="Da-2h2B4faU",
                categoria="theories"
            ),
            VideoCosmico(
                titulo="Multiversos: ¿Existen Universos Paralelos?",
                descripcion="Exploración de la teoría del multiverso y las implicaciones de la existencia de universos paralelos.",
                youtube_id="Ywn2Lz5zmYg",
                categoria="theories"
            ),
            VideoCosmico(
                titulo="Cosmología en la Filosofía Antigua",
                descripcion="Un recorrido por las visiones cosmológicas de las antiguas civilizaciones y cómo comprendían el universo.",
                youtube_id="gSKzgpt4HBU",
                categoria="philosophy"
            ),
            VideoCosmico(
                titulo="La Relatividad del Tiempo: Explicación de Einstein",
                descripcion="Explicación clara de cómo la teoría de la relatividad de Einstein cambió nuestra comprensión del tiempo.",
                youtube_id="TgH9KXEQ0YU",
                categoria="space_time"
            ),
            VideoCosmico(
                titulo="Agujeros Negros: Los Monstruos del Universo",
                descripcion="Todo lo que necesitas saber sobre los agujeros negros y sus propiedades fascinantes.",
                youtube_id="e-P5IFTqB98",
                categoria="space_time"
            )
        ]
        db.session.add_all(videos)
        
        # Add cosmic images
        imagenes = [
            ImagenCosmica(
                titulo="Representación del Big Bang",
                descripcion="Ilustración artística del momento inicial del universo conocido como el Big Bang.",
                url="https://images.unsplash.com/photo-1462331940025-496dfbfc7564",
                fuente="NASA/ESA",
                categoria="big_bang"
            ),
            ImagenCosmica(
                titulo="Primera Luz del Universo",
                descripcion="Imagen de la radiación de fondo de microondas cósmico, la luz residual del Big Bang.",
                url="https://images.unsplash.com/photo-1465101162946-4377e57745c3",
                fuente="WMAP/NASA",
                categoria="big_bang"
            ),
            ImagenCosmica(
                titulo="Visualización de la Teoría de Cuerdas",
                descripcion="Representación artística de las cuerdas vibrantes que, según la teoría, componen la materia fundamental.",
                url="https://images.unsplash.com/photo-1496065187959-7f07b8353c55",
                fuente="Science Photo Library",
                categoria="theories"
            ),
            ImagenCosmica(
                titulo="Concepto de Multiverso",
                descripcion="Ilustración artística del concepto de múltiples universos existiendo en paralelo.",
                url="https://images.unsplash.com/photo-1451187580459-43490279c0fa",
                fuente="Scientific American",
                categoria="theories"
            ),
            ImagenCosmica(
                titulo="Mapa Cosmológico Antiguo",
                descripcion="Representación de un mapa cosmológico de la antigua Grecia mostrando su concepción del universo.",
                url="https://images.unsplash.com/photo-1454789476662-53eb23ba5907",
                fuente="Biblioteca Nacional",
                categoria="philosophy"
            ),
            ImagenCosmica(
                titulo="Ilustración del Espacio-Tiempo Curvo",
                descripcion="Visualización de cómo la masa curva el tejido del espacio-tiempo según la relatividad general.",
                url="https://images.unsplash.com/photo-1506703719100-a0b3a3a7f209",
                fuente="Science Magazine",
                categoria="space_time"
            ),
            ImagenCosmica(
                titulo="Primera Imagen Real de un Agujero Negro",
                descripcion="La histórica primera imagen de un agujero negro, capturada por el Event Horizon Telescope en 2019.",
                url="https://images.unsplash.com/photo-1534270804882-6b5048b1c1fc",
                fuente="Event Horizon Telescope",
                categoria="space_time"
            ),
            ImagenCosmica(
                titulo="Galaxia en Espiral",
                descripcion="Impresionante imagen de una galaxia espiral similar a nuestra Vía Láctea.",
                url="https://images.unsplash.com/photo-1539321908154-04927596764d",
                fuente="Hubble Space Telescope",
                categoria="space_time"
            )
        ]
        db.session.add_all(imagenes)
        
        db.session.commit()

# Ejecutar la inicialización de la base de datos al importar el módulo
with app.app_context():
    initialize_db()
