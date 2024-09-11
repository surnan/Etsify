from app.models import db, ProductImage, environment, SCHEMA
# from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_product_images():
    pic1 = ProductImage(
       productId = 1, image_url="https://cdn.sanity.io/images/tlr8oxjg/production/7b7f05720074a848850e0705779306c27da5a6cf-1065x597.png?w=3840&q=100&fit=clip&auto=format")
    pic2= ProductImage(
        productId = 1, image_url="https://cdn.sanity.io/images/tlr8oxjg/production/7b7f05720074a848850e0705779306c27da5a6cf-1065x597.png?w=3840&q=100&fit=clip&auto=format")
    pic3 = ProductImage(
       productId = 1, image_url="https://cdn.sanity.io/images/tlr8oxjg/production/7b7f05720074a848850e0705779306c27da5a6cf-1065x597.png?w=3840&q=100&fit=clip&auto=format")
    pic4 = ProductImage(
       productId = 1, image_url="https://cdn.sanity.io/images/tlr8oxjg/production/7b7f05720074a848850e0705779306c27da5a6cf-1065x597.png?w=3840&q=100&fit=clip&auto=format")
    pic5= ProductImage(
       productId = 1, image_url="https://cdn.sanity.io/images/tlr8oxjg/production/7b7f05720074a848850e0705779306c27da5a6cf-1065x597.png?w=3840&q=100&fit=clip&auto=format")
    pic6 = ProductImage(
        productId = 2, image_url="https://cdn.sanity.io/images/tlr8oxjg/production/7b7f05720074a848850e0705779306c27da5a6cf-1065x597.png?w=3840&q=100&fit=clip&auto=format")
    pic7 = ProductImage(
       productId = 2, image_url = "https://cdn.sanity.io/images/tlr8oxjg/production/7b7f05720074a848850e0705779306c27da5a6cf-1065x597.png?w=3840&q=100&fit=clip&auto=format")
    pic8 = ProductImage(
       productId = 2, image_url="https://cdn.sanity.io/images/tlr8oxjg/production/7b7f05720074a848850e0705779306c27da5a6cf-1065x597.png?w=3840&q=100&fit=clip&auto=format")
    pic9 = ProductImage(
       productId = 2, image_url="https://cdn.sanity.io/images/tlr8oxjg/production/7b7f05720074a848850e0705779306c27da5a6cf-1065x597.png?w=3840&q=100&fit=clip&auto=format")
    pic10 = ProductImage(
       productId = 2, image_url="https://cdn.sanity.io/images/tlr8oxjg/production/7b7f05720074a848850e0705779306c27da5a6cf-1065x597.png?w=3840&q=100&fit=clip&auto=format")
    

    db.session.add(pic1)
    db.session.add(pic2)
    db.session.add(pic3)
    db.session.add(pic4)
    db.session.add(pic5)
    db.session.add(pic6)
    db.session.add(pic7)
    db.session.add(pic8)
    db.session.add(pic9)
    db.session.add(pic10)
    db.session.commit()

def undo_product_images():
   if environment == "production":
      db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
   # else:
   #    db.session.execute(text("DELETE FROM order_products"))
   #    db.session.execute(text("DELETE FROM orders"))
      
   db.session.commit()