# از یک ایمیج پایتون استفاده کنید
FROM python:3.9-slim

# تنظیم دایرکتوری کاری
WORKDIR /app

# به‌روزرسانی pip
RUN pip install --upgrade pip

# نصب وابستگی‌ها
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# کپی پروژه به داخل کانتینر
COPY . /app/

# اجرا کردن فرمان مهاجرت‌ها و استاتیک‌ها
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput

# تنظیم پورت و اجرای سرور
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
