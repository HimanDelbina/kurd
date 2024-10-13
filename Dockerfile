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

# تنظیم پورت
EXPOSE 8000

# تنظیم CMD برای انجام مهاجرت‌ها و استاتیک‌ها در زمان اجرا
CMD ["sh", "-c", "python manage.py migrate && python manage.py collectstatic --noinput && python manage.py runserver 0.0.0.0:8000"]
