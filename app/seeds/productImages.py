from app.models import db, ProductImage, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_product_images():
   pic1 = ProductImage(
      productId = 1, image_url="https://m.media-amazon.com/images/I/81i4Qoc43PS.jpg")
   pic2= ProductImage(
      productId = 1, image_url="https://rainbowplantlife.com/wp-content/uploads/2022/09/Mexican-Black-Beans-cover-photo-1-of-1-500x500.jpg")
   pic3 = ProductImage(
      productId = 1, image_url="https://www.daringgourmet.com/wp-content/uploads/2020/08/Baked-Beans-20.jpg")
   pic4 = ProductImage(
      productId = 1, image_url="https://cdn.loveandlemons.com/wp-content/uploads/2021/02/black-bean-recipes.jpg")
   pic5= ProductImage(
      productId = 1, image_url="https://belleofthekitchen.com/wp-content/uploads/2018/06/mexican-black-beans-square.jpg")
   pic6 = ProductImage(
      productId = 2, image_url="https://www.avidacbd.com/wp-content/uploads/2023/06/500_Blue_Razz_cbd_vape.jpg")
   pic7 = ProductImage(
      productId = 2, image_url = "https://www.redstarvapor.com/wp-content/uploads/2023/10/GeekBar-Pulse.jpg")
   pic8 = ProductImage(
      productId = 2, image_url="https://eliquidstop.com/cdn/shop/files/smok-priv-bar-turbo-15000-puffs-vape-disposable-anti-leak-tech-eliquidstop-3_700x700.jpg?v=1704943825")
   pic9 = ProductImage(
      productId = 2, image_url="https://infiniterecovery1.b-cdn.net/wp-content/uploads/2023/01/from-squarespace-14754-AdobeStock_113130199.jpeg")
   pic10 = ProductImage(
      productId = 2, image_url="https://www.huffandpuffers.com/cdn/shop/files/raz-tn9000-disposable-vape-pineapple-passionfruit-guava.jpg?v=1711046083&width=1000")
   pic11 = ProductImage(
      productId = 3, image_url="https://hips.hearstapps.com/hmg-prod/images/2024-tesla-cybertruck-115-65e8945de87ba.jpg")
   pic12 = ProductImage(
      productId = 3, image_url="https://www.greendrive-accessories.com/blog/wp-content/uploads/2024/01/Tesla-Cybertruck-Towing-Prowess-and-Range-Revelations.png")
   pic13 = ProductImage(
      productId = 3, image_url="https://images.hindustantimes.com/auto/img/2023/12/01/600x338/Tesla_Cybertruck_4_1701399142651_1701400983502.jpg")
   pic14 = ProductImage(
      productId = 3, image_url="https://www.ttnews.com/sites/default/files/styles/convert_to_webp/public/2024-02/Cybertruck-Interior-650.jpg.webp")
   pic15 = ProductImage(
      productId = 3, image_url="https://picolio.auto123.com/auto123-media/articles/2023/11/70954/tesla-cybertruck-xiaohongshu-weibo-002fr.jpg?scaledown=450")

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
   db.session.add(pic11)
   db.session.add(pic12)
   db.session.add(pic13)
   db.session.add(pic14)
   db.session.add(pic15)
   db.session.commit()

def undo_product_images():
   if environment == "production":
      db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
   else:
      db.session.execute(text("DELETE FROM order_products"))
      db.session.execute(text("DELETE FROM orders"))
      
   db.session.commit()