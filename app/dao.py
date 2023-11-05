def get_categories():
    return [{
        'id': 1,
        'name': 'Mobile'
    }, {
        'id': 2,
        'name': 'Tablet'
    }]


def get_products(kw):
    products = [{
        "id": 1,
        "name": "Iphone 13",
        "price": 20000000,
        "image": "https://www.google.com.vn/imgres?imgurl=https%3A%2F%2Fcdn2.cellphones.com.vn%2Fx%2Fmedia%2Fcatalog%2Fproduct%2F3%2F_%2F3_51_1_2_2_1_1_2_1_1.jpg&tbnid=GIsh0VBtfKYUkM&vet=12ahUKEwjX2r6Q9qyCAxUsZ_UHHdPNDW0QMygAegQIARB9..i&imgrefurl=https%3A%2F%2Fcellphones.com.vn%2Fiphone-13-pro-max-128gb-cu-tray-xuoc.html&docid=hdHcM3_Imge9LM&w=800&h=800&q=iphone%2013&ved=2ahUKEwjX2r6Q9qyCAxUsZ_UHHdPNDW0QMygAegQIARB9https://www.google.com.vn/imgres?imgurl=https%3A%2F%2Fcdn2.cellphones.com.vn%2Fx%2Fmedia%2Fcatalog%2Fproduct%2F3%2F_%2F3_51_1_2_2_1_1_2_1_1.jpg&tbnid=GIsh0VBtfKYUkM&vet=12ahUKEwjX2r6Q9qyCAxUsZ_UHHdPNDW0QMygAegQIARB9..i&imgrefurl=https%3A%2F%2Fcellphones.com.vn%2Fiphone-13-pro-max-128gb-cu-tray-xuoc.html&docid=hdHcM3_Imge9LM&w=800&h=800&q=iphone%2013&ved=2ahUKEwjX2r6Q9qyCAxUsZ_UHHdPNDW0QMygAegQIARB9",
        "category_id": 1

    }, {
        "id": 1,
        "name": "Galaxy",
        "price": 25000000,
        "image": "https://www.google.com.vn/imgres?imgurl=https%3A%2F%2Fcdn2.cellphones.com.vn%2Fx%2Fmedia%2Fcatalog%2Fproduct%2F3%2F_%2F3_51_1_2_2_1_1_2_1_1.jpg&tbnid=GIsh0VBtfKYUkM&vet=12ahUKEwjX2r6Q9qyCAxUsZ_UHHdPNDW0QMygAegQIARB9..i&imgrefurl=https%3A%2F%2Fcellphones.com.vn%2Fiphone-13-pro-max-128gb-cu-tray-xuoc.html&docid=hdHcM3_Imge9LM&w=800&h=800&q=iphone%2013&ved=2ahUKEwjX2r6Q9qyCAxUsZ_UHHdPNDW0QMygAegQIARB9https://www.google.com.vn/imgres?imgurl=https%3A%2F%2Fcdn2.cellphones.com.vn%2Fx%2Fmedia%2Fcatalog%2Fproduct%2F3%2F_%2F3_51_1_2_2_1_1_2_1_1.jpg&tbnid=GIsh0VBtfKYUkM&vet=12ahUKEwjX2r6Q9qyCAxUsZ_UHHdPNDW0QMygAegQIARB9..i&imgrefurl=https%3A%2F%2Fcellphones.com.vn%2Fiphone-13-pro-max-128gb-cu-tray-xuoc.html&docid=hdHcM3_Imge9LM&w=800&h=800&q=iphone%2013&ved=2ahUKEwjX2r6Q9qyCAxUsZ_UHHdPNDW0QMygAegQIARB9",
        "category_id": 1

    }, {
        "id": 1,
        "name": "Galaxy",
        "price": 25000000,
        "image": "https://www.google.com.vn/imgres?imgurl=https%3A%2F%2Fcdn2.cellphones.com.vn%2Fx%2Fmedia%2Fcatalog%2Fproduct%2F3%2F_%2F3_51_1_2_2_1_1_2_1_1.jpg&tbnid=GIsh0VBtfKYUkM&vet=12ahUKEwjX2r6Q9qyCAxUsZ_UHHdPNDW0QMygAegQIARB9..i&imgrefurl=https%3A%2F%2Fcellphones.com.vn%2Fiphone-13-pro-max-128gb-cu-tray-xuoc.html&docid=hdHcM3_Imge9LM&w=800&h=800&q=iphone%2013&ved=2ahUKEwjX2r6Q9qyCAxUsZ_UHHdPNDW0QMygAegQIARB9https://www.google.com.vn/imgres?imgurl=https%3A%2F%2Fcdn2.cellphones.com.vn%2Fx%2Fmedia%2Fcatalog%2Fproduct%2F3%2F_%2F3_51_1_2_2_1_1_2_1_1.jpg&tbnid=GIsh0VBtfKYUkM&vet=12ahUKEwjX2r6Q9qyCAxUsZ_UHHdPNDW0QMygAegQIARB9..i&imgrefurl=https%3A%2F%2Fcellphones.com.vn%2Fiphone-13-pro-max-128gb-cu-tray-xuoc.html&docid=hdHcM3_Imge9LM&w=800&h=800&q=iphone%2013&ved=2ahUKEwjX2r6Q9qyCAxUsZ_UHHdPNDW0QMygAegQIARB9",
        "category_id": 1

    }, {
        "id": 1,
        "name": "Galaxy",
        "price": 25000000,
        "image": "https://www.google.com.vn/imgres?imgurl=https%3A%2F%2Fcdn2.cellphones.com.vn%2Fx%2Fmedia%2Fcatalog%2Fproduct%2F3%2F_%2F3_51_1_2_2_1_1_2_1_1.jpg&tbnid=GIsh0VBtfKYUkM&vet=12ahUKEwjX2r6Q9qyCAxUsZ_UHHdPNDW0QMygAegQIARB9..i&imgrefurl=https%3A%2F%2Fcellphones.com.vn%2Fiphone-13-pro-max-128gb-cu-tray-xuoc.html&docid=hdHcM3_Imge9LM&w=800&h=800&q=iphone%2013&ved=2ahUKEwjX2r6Q9qyCAxUsZ_UHHdPNDW0QMygAegQIARB9https://www.google.com.vn/imgres?imgurl=https%3A%2F%2Fcdn2.cellphones.com.vn%2Fx%2Fmedia%2Fcatalog%2Fproduct%2F3%2F_%2F3_51_1_2_2_1_1_2_1_1.jpg&tbnid=GIsh0VBtfKYUkM&vet=12ahUKEwjX2r6Q9qyCAxUsZ_UHHdPNDW0QMygAegQIARB9..i&imgrefurl=https%3A%2F%2Fcellphones.com.vn%2Fiphone-13-pro-max-128gb-cu-tray-xuoc.html&docid=hdHcM3_Imge9LM&w=800&h=800&q=iphone%2013&ved=2ahUKEwjX2r6Q9qyCAxUsZ_UHHdPNDW0QMygAegQIARB9",
        "category_id": 1

    }]

    if kw:
        products = [ p for p in products if p['name'].find(kw) >= 0 ]

    return products



