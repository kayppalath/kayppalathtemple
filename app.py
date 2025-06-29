from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory
from werkzeug.utils import secure_filename
import os
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Ensure upload directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Allowed file extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'pdf'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Sample temple data - you can modify this with your actual temple information
TEMPLE_DATA = {
    'name': 'Kayppalath Temple',
    'deity': 'Lord Shiva',
    'location': 'Kerala, India',
    'established': 'Ancient times',
    'description': 'A sacred temple with deep spiritual significance and rich cultural heritage.',
    'history': '''
    The Kayppalath Temple stands as a testament to centuries of devotion and spiritual practice. 
    Founded in ancient times, this sacred place has been a center of worship, meditation, and 
    community gathering for generations. The temple's architecture reflects the traditional 
    Kerala style, with intricate carvings and spiritual symbolism adorning its walls.
    
    Throughout its history, the temple has witnessed countless ceremonies, festivals, and 
    moments of divine connection. It has served as a beacon of hope and spiritual guidance 
    for devotees from all walks of life, offering solace and strength through prayer and 
    meditation.
    
    The temple's significance extends beyond religious practice, encompassing cultural 
    preservation, community bonding, and the transmission of ancient wisdom to future 
    generations. Each stone, each carving, and each ritual carries the weight of tradition 
    and the promise of spiritual renewal.
    ''',
    'deity_significance': '''
    Lord Shiva, the presiding deity of Kayppalath Temple, represents the eternal cycle of 
    creation, preservation, and dissolution. As the destroyer of ignorance and ego, Shiva 
    guides devotees toward spiritual enlightenment and inner transformation.
    
    The deity's presence in this temple is believed to bestow blessings of peace, wisdom, 
    and liberation. Devotees come seeking divine intervention, spiritual guidance, and the 
    strength to overcome life's challenges through faith and devotion.
    
    The temple's rituals and ceremonies are designed to honor Shiva's various aspects - 
    from the peaceful family man to the fierce destroyer of evil. Each offering and prayer 
    is a step toward spiritual growth and divine connection.
    '''
}

# Sample photos data - you can replace with actual photos
SAMPLE_PHOTOS = [
    {
        'id': 1,
        'title': 'Temple Entrance',
        'description': 'The majestic entrance of Kayppalath Temple',
        'filename': 'temple_entrance.jpg',
        'date': '2023-01-15',
        'category': 'Architecture'
    },
    {
        'id': 2,
        'title': 'Sacred Sanctum',
        'description': 'The inner sanctum where the main deity resides',
        'filename': 'sanctum.jpg',
        'date': '2023-02-20',
        'category': 'Interior'
    },
    {
        'id': 3,
        'title': 'Festival Celebration',
        'description': 'Annual temple festival with traditional rituals',
        'filename': 'festival.jpg',
        'date': '2023-03-10',
        'category': 'Events'
    }
]

@app.route('/')
def home():
    return render_template('home.html', temple=TEMPLE_DATA)

@app.route('/about')
def about():
    return render_template('about.html', temple=TEMPLE_DATA)

@app.route('/photos')
def photos():
    # Get actual photos from upload folder
    photos = []
    if os.path.exists(app.config['UPLOAD_FOLDER']):
        for filename in os.listdir(app.config['UPLOAD_FOLDER']):
            if allowed_file(filename):
                photos.append({
                    'id': len(photos) + 1,
                    'title': filename.replace('_', ' ').replace('.', ' ').title(),
                    'description': f'Historical photo from {filename}',
                    'filename': filename,
                    'date': datetime.fromtimestamp(
                        os.path.getctime(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                    ).strftime('%Y-%m-%d'),
                    'category': 'Historical'
                })
    
    # Add sample photos if no uploaded photos exist
    if not photos:
        photos = SAMPLE_PHOTOS
    
    return render_template('photos.html', photos=photos)

@app.route('/upload', methods=['GET', 'POST'])
def upload_photo():
    if request.method == 'POST':
        if 'photo' not in request.files:
            flash('No file selected')
            return redirect(request.url)
        
        file = request.files['photo']
        if file.filename == '':
            flash('No file selected')
            return redirect(request.url)
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            # Add timestamp to avoid filename conflicts
            name, ext = os.path.splitext(filename)
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f"{name}_{timestamp}{ext}"
            
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash('Photo uploaded successfully!')
            return redirect(url_for('photos'))
        else:
            flash('Invalid file type. Please upload images or PDFs only.')
    
    return render_template('upload.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 