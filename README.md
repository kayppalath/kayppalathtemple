# Kayppalath Temple Digital Heritage Website

A modern, responsive web application built with Python Flask to showcase the history, spiritual legacy, and archival photographs of Kayppalath Temple.

## Features

### 🏛️ About Page
- **Temple History**: Comprehensive overview of the temple's ancient origins and spiritual significance
- **Deity Significance**: Detailed information about Lord Shiva and the temple's spiritual importance
- **Temple Features**: Information about architecture, rituals, and community services
- **Visiting Information**: Opening hours and location details

### 📸 Photos Gallery
- **Digital Archive**: Display of archival photographs and historical documents
- **Upload System**: Easy-to-use interface for adding new photos and documents
- **Categorized Display**: Organized gallery with different categories (Architecture, Rituals, Events, Historical)
- **PDF Support**: View and download historical documents
- **Responsive Design**: Beautiful gallery layout that works on all devices

### 🎨 Modern Design
- **Responsive Layout**: Works perfectly on desktop, tablet, and mobile devices
- **Sacred Color Scheme**: Traditional temple-inspired colors and design elements
- **Beautiful Typography**: Elegant fonts and professional styling
- **Interactive Elements**: Hover effects and smooth animations

## Technology Stack

- **Backend**: Python Flask
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Icons**: Font Awesome
- **Fonts**: Google Fonts (Playfair Display, Poppins)
- **File Handling**: Werkzeug for secure file uploads

## Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Step 1: Clone the Repository
```bash
git clone <repository-url>
cd kayppalathtemple
```

### Step 2: Create Virtual Environment (Recommended)
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run the Application
```bash
python app.py
```

### Step 5: Access the Website
Open your web browser and navigate to:
```
http://localhost:5000
```

## Project Structure

```
kayppalathtemple/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── templates/            # HTML templates
│   ├── base.html         # Base template with navigation
│   ├── home.html         # Home page
│   ├── about.html        # About page
│   ├── photos.html       # Photo gallery
│   └── upload.html       # Upload form
└── static/               # Static files
    └── uploads/          # Uploaded photos and documents
```

## Usage Guide

### Adding Temple Information
Edit the `TEMPLE_DATA` dictionary in `app.py` to customize:
- Temple name and location
- Deity information
- Historical details
- Spiritual significance

### Uploading Photos
1. Navigate to the Photos page
2. Click "Upload Photo" button
3. Select your file (JPG, PNG, GIF, or PDF)
4. File will be automatically categorized and displayed

### Supported File Types
- **Images**: JPG, JPEG, PNG, GIF
- **Documents**: PDF
- **Maximum Size**: 16MB per file

## Customization

### Changing Colors
Edit the CSS variables in `templates/base.html`:
```css
:root {
    --primary-color: #8B4513;    /* Main temple color */
    --secondary-color: #D2691E;  /* Secondary color */
    --accent-color: #FFD700;     /* Accent color */
}
```

### Adding New Pages
1. Create a new template in `templates/`
2. Add a route in `app.py`
3. Update navigation in `templates/base.html`

## Security Features

- **Secure File Uploads**: File type validation and secure filename handling
- **File Size Limits**: 16MB maximum file size
- **XSS Protection**: Flask's built-in security features
- **CSRF Protection**: Form security measures

## Deployment

### Local Development
```bash
python app.py
```

### Production Deployment
For production deployment, consider:
- Using a production WSGI server (Gunicorn, uWSGI)
- Setting up a reverse proxy (Nginx)
- Using environment variables for configuration
- Implementing proper logging and monitoring

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is dedicated to the spiritual heritage of Kayppalath Temple.

## Support

For questions or support, please contact the temple administration.

---

**Om Namah Shivaya** 🙏
