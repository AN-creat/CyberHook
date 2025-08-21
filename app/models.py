
from datetime import datetime
from . import db

class Victim(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120))
    username = db.Column(db.String(120))
    phone =db.Column(db.String(10), nullable=True)
    ip_address = db.Column(db.String(45))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    link_clicks = db.Column(db.Integer, default=1)
    phishing_count = db.Column(db.Integer, default=1)
    awareness_completed = db.Column(db.Boolean, default=False)  # ✅ تم التوعية

def mask_email(email):
    if not email or '@' not in email:
        return email
    name, domain = email.split('@')
    masked_name = name[:3] + '***' if len(name) > 3 else name + '***'
    
    domain_parts = domain.split('.')
    if len(domain_parts) >= 2:
        main_domain = domain_parts[0]  # example
        tld = domain_parts[-1]          # com
        masked_domain = main_domain + '.' + tld
    else:
        masked_domain = domain

    return masked_name + '@' + masked_domain

def mask_phone(phone):
    if not phone or len(phone) < 10:
        return phone or "غير متوفر"
    return phone[:3] + '****' + phone[-3:]

from . import db

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
