from app import create_app, db
from app.models import Victim
from sqlalchemy import inspect, text

# إنشاء سياق التطبيق
app = create_app()
with app.app_context():
    inspector = inspect(db.engine)
    columns = [col['name'] for col in inspector.get_columns('victim')]

    # تحقق إذا كان العمود موجود
    if 'phone' not in columns:
        print("إضافة العمود 'phone' للجدول victim...")
        with db.engine.connect() as conn:
            conn.execute(text('ALTER TABLE victim ADD COLUMN phone VARCHAR(10);'))
            conn.commit()
    else:
        print("العمود 'phone' موجود بالفعل.")

    # تعبئة القيم الفارغة بالقيمة الافتراضية
    victims = Victim.query.all()
    for v in victims:
        if not v.phone:
            v.phone = "غير متوفر"
    db.session.commit()
    print("تم تحديث القيم الفارغة في العمود 'phone'.")
