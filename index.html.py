<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vape Shop Mini App</title>
    <script src="https://telegram.org/js/telegram-web-app.js"></script>
    <style>
        body { font-family: sans-serif; background: #1a1a1a; color: white; margin: 0; padding: 15px; }
        .category { margin-bottom: 20px; border-bottom: 1px solid #333; padding-bottom: 10px; }
        .category h2 { color: #0088cc; font-size: 1.2rem; }
        .item { display: flex; justify-content: space-between; align-items: center; background: #2c2c2c; padding: 10px; margin: 5px 0; border-radius: 8px; }
        .price { color: #4CAF50; font-weight: bold; }
        button { background: #0088cc; border: none; color: white; padding: 5px 10px; border-radius: 5px; cursor: pointer; }
        .cart-btn { position: fixed; bottom: 20px; width: calc(100% - 30px); padding: 15px; background: #4CAF50; border: none; color: white; font-weight: bold; border-radius: 10px; }
    </style>
</head>
<body>

    <div id="app">
        <h1>Vape Shop</h1>
        
        <!-- Секция Жидкости -->
        <div class="category">
            <h2>Жидкости</h2>
            <div class="item"><span>YUMMY (17р)</span><button onclick="addToCart('YUMMY', 17)">+</button></div>
            <div class="item"><span>ЗЛОЙ МОНАХ (20р)</span><button onclick="addToCart('Злой Монах', 20)">+</button></div>
            <div class="item"><span>Podonki V1 (15р)</span><button onclick="addToCart('Podonki V1', 15)">+</button></div>
            <div class="item"><span>Podonki Podgon (15р)</span><button onclick="addToCart('Podonki Podgon', 15)">+</button></div>
            <div class="item"><span>ANNIMA LOVE (17р)</span><button onclick="addToCart('ANNIMA', 17)">+</button></div>
            <div class="item"><span>MAD & Самоубийца (20р)</span><button onclick="addToCart('MAD', 20)">+</button></div>
            <div class="item"><span>Cats Dota / Will (17р)</span><button onclick="addToCart('Cats', 17)">+</button></div>
            <div class="item"><span>Рик и Морти (17р)</span><button onclick="addToCart('Рик и Морти', 17)">+</button></div>
        </div>

        <!-- Одноразки -->
        <div class="category">
            <h2>Одноразки</h2>
            <div class="item"><span>Elfbar MOONNIGHT 40k (45р)</span><button onclick="addToCart('Elfbar 40k', 45)">+</button></div>
            <div class="item"><span>GTMBAR TURBO 30k (45р)</span><button onclick="addToCart('GTMBAR 30k', 45)">+</button></div>
        </div>

        <!-- Расходники -->
        <div class="category">
            <h2>Расходники / Поды</h2>
            <div class="item"><span>Картридж Ватруха (13р)</span><button onclick="addToCart('Картридж V.Thru', 13)">+</button></div>
            <div class="item"><span>Картридж XROS (12р)</span><button onclick="addToCart('Картридж XROS', 12)">+</button></div>
            <div class="item"><span>Испаритель Hero 0.4 (12р)</span><button onclick="addToCart('Испар Hero', 12)">+</button></div>
            <div class="item"><span>AEGIS HERO H45 (110р)</span><button onclick="addToCart('H45', 110)">+</button></div>
            <div class="item"><span>AEGIS BOOST 3 (120р)</span><button onclick="addToCart('Boost 3', 120)">+</button></div>
        </div>

        <!-- Снюс -->
        <div class="category">
            <h2>Снюс</h2>
            <div class="item"><span>FAFF 150мг (15р)</span><button onclick="addToCart('FAFF', 15)">+</button></div>
        </div>
    </div>

    <button class="cart-btn" onclick="sendOrder()">Оформить заказ</button>

    <script>
        let tg = window.Telegram.WebApp;
        tg.expand(); // Расширить на весь экран

        let cart = [];

        function addToCart(name, price) {
            cart.push({name, price});
            tg.HapticFeedback.impactOccurred('light'); // Виброотклик
            alert("Добавлено: " + name);
        }

        function sendOrder() {
            if (cart.length === 0) return alert("Корзина пуста!");
            
            let text = "Новый заказ:\n";
            let total = 0;
            cart.forEach(item => {
                text += `- ${item.name}: ${item.price}р\n`;
                total += item.price;
            });
            text += `\nИтого: ${total}р`;

            // Отправляем данные боту
            tg.sendData(text);
            tg.close();
        }
    </script>
</body>
</html>  
