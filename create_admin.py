from app import db, create_app
from app.models import Admin
from werkzeug.security import generate_password_hash

# إنشاء التطبيق
app = create_app()

with app.app_context():
    # إدخال بيانات المشرف من المستخدم
    username = input("أدخل اسم المستخدم للمشرف: ").strip()
    password = input("أدخل كلمة المرور للمشرف: ").strip()

    # التحقق إذا كان المشرف موجود
    existing_admin = Admin.query.filter_by(username=username).first()
    if existing_admin:
        print(f"⚠ المشرف '{username}' موجود مسبقًا، لم يتم إنشاؤه مرة أخرى.")
    else:
        hashed_password = generate_password_hash(password)
        new_admin = Admin(username=username, password=hashed_password)
        db.session.add(new_admin)
        db.session.commit()
        print(f"✅ تم إنشاء حساب المشرف '{username}' بنجاح.")
