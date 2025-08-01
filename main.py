<!DOCTYPE html>
<html lang="uk">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Lux Car Parfum</title>
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap" rel="stylesheet"/>
  <style>
    body {
      margin: 0;
      font-family: 'Montserrat', sans-serif;
      background: #f7f7f7;
      color: #333;
    }
    header {
      background: #111;
      color: #fff;
      padding: 2rem;
      text-align: center;
    }
    header h1 {
      margin: 0;
      font-size: 2.5rem;
    }
    header p {
      font-size: 1.2rem;
    }
    nav {
      display: flex;
      justify-content: center;
      background: #222;
      padding: 1rem 0;
    }
    nav a {
      color: #fff;
      text-decoration: none;
      margin: 0 1rem;
      font-weight: bold;
    }
    section {
      padding: 3rem 1.5rem;
      max-width: 1200px;
      margin: auto;
    }
    .products {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
      gap: 2rem;
    }
    .product {
      background: #fff;
      border-radius: 12px;
      padding: 1rem;
      box-shadow: 0 4px 12px rgba(0,0,0,0.1);
      text-align: center;
    }
    .product img {
      max-width: 100%;
      border-radius: 8px;
    }
    .product h3 {
      margin: 0.5rem 0;
    }
    footer {
      background: #111;
      color: #fff;
      text-align: center;
      padding: 2rem 1rem;
    }
    .cta {
      background: #ffcf33;
      color: #000;
      text-align: center;
      padding: 2rem 1rem;
      font-size: 1.4rem;
      font-weight: bold;
    }
    .cta a {
      display: inline-block;
      background: #000;
      color: #fff;
      padding: 0.8rem 1.5rem;
      margin-top: 1rem;
      text-decoration: none;
      border-radius: 8px;
    }
  </style>
</head>
<body>

  <header>
    <h1>Lux Car Parfum</h1>
    <p>Аксесуари та засоби для догляду за вашим авто</p>
  </header>

  <nav>
    <a href="#products">Товари</a>
    <a href="#about">Про нас</a>
    <a href="#contact">Контакти</a>
  </nav>

  <section class="cta">
    🚗 Насолода для твого авто кожного дня!<br />
    <a href="https://www.instagram.com/lux_car_parfum/" target="_blank">Перейти в Instagram</a>
  </section>

  <section id="products">
    <h2>Популярні товари</h2>
    <div class="products">
      <div class="product">
        <img src="https://via.placeholder.com/300x200?text=Ароматизатор" alt="Ароматизатор" />
        <h3>Ароматизатори</h3>
        <p>Різноманітні аромати для авто преміум-класу.</p>
      </div>
      <div class="product">
        <img src="https://via.placeholder.com/300x200?text=Автохімія" alt="Автохімія" />
        <h3>Автохімія</h3>
        <p>Чистота та блиск для вашого авто всередині і ззовні.</p>
      </div>
      <div class="product">
        <img src="https://via.placeholder.com/300x200?text=Аксесуари" alt="Аксесуари" />
        <h3>Аксесуари</h3>
        <p>Дрібниці, які створюють комфорт і стиль.</p>
      </div>
    </div>
  </section>

  <section id="about">
    <h2>Про нас</h2>
    <p>
      Lux Car Parfum — це український магазин, який спеціалізується на продажу якісних ароматизаторів, автохімії та аксесуарів.
      Ми допомагаємо зробити кожну поїздку приємнішою завдяки деталям, які мають значення.
    </p>
  </section>

  <section id="contact">
    <h2>Контакти</h2>
    <p>📱 Пишіть нам в Instagram: <a href="https://www.instagram.com/lux_car_parfum/" target="_blank">@lux_car_parfum</a></p>
    <p>📦 Доставка по всій Україні Новою Поштою</p>
  </section>

  <footer>
    <p>&copy; 2025 Lux Car Parfum. Всі права захищені.</p>
  </footer>

</body>
</html>
