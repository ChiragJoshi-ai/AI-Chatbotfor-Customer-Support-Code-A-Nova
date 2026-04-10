"""
knowledge_base.py
Predefined intents, patterns, and responses for the customer support chatbot.
"""

KNOWLEDGE_BASE = {
    "greeting": {
        "patterns": [
            "hello", "hi", "hey", "good morning", "good evening",
            "good afternoon", "howdy", "what's up", "sup", "greetings"
        ],
        "responses": [
            "Hey there! 👋 How can I help you today?",
            "Hi! Welcome to support. What can I do for you?",
            "Hello! I'm here to help. What's on your mind?"
        ]
    },

    "goodbye": {
        "patterns": [
            "bye", "goodbye", "see you", "later", "take care",
            "thanks bye", "that's all", "exit", "quit", "done"
        ],
        "responses": [
            "Goodbye! Have a great day! 😊",
            "Take care! Feel free to come back if you need anything.",
            "See you later! Hope I was helpful."
        ]
    },

    "thanks": {
        "patterns": [
            "thank you", "thanks", "thx", "thank u", "appreciate it",
            "cheers", "many thanks", "great thanks"
        ],
        "responses": [
            "You're welcome! 😊 Anything else I can help with?",
            "Happy to help! Let me know if there's anything else.",
            "Of course! Is there anything else you need?"
        ]
    },

    "order_status": {
        "patterns": [
            "where is my order", "order status", "track my order",
            "track order", "order tracking", "when will my order arrive",
            "order not received", "order shipped", "shipping status",
            "delivery status", "where is my package", "my order"
        ],
        "responses": [
            "To track your order, please visit our website and enter your order ID in the 'Track Order' section. You can also check your confirmation email for a tracking link.",
            "You can track your order by logging into your account and navigating to 'My Orders'. If you don't see an update within 24 hours of ordering, feel free to contact us.",
            "Order tracking is available on our website under 'My Account → Orders'. Your tracking number was also sent to your email when the order shipped."
        ]
    },

    "refund": {
        "patterns": [
            "refund", "money back", "return", "get my money back",
            "want a refund", "refund policy", "return policy",
            "cancel order", "exchange", "return item"
        ],
        "responses": [
            "We offer a 30-day return policy. To initiate a refund, go to 'My Orders', select the item, and click 'Request Return'. Refunds are processed within 5-7 business days.",
            "You can request a refund within 30 days of purchase. Visit the returns section on our website or email support@store.com with your order number.",
            "Our refund process is simple — just log in, go to your order history, and select 'Return or Exchange'. Refunds hit your account in 5-7 business days."
        ]
    },

    "payment": {
        "patterns": [
            "payment", "pay", "payment method", "credit card", "debit card",
            "upi", "payment failed", "payment issue", "not able to pay",
            "payment options", "accepted payments", "how to pay"
        ],
        "responses": [
            "We accept Visa, Mastercard, UPI, Net Banking, and all major wallets. If your payment failed, please try again or use a different payment method.",
            "Payment methods available: Credit/Debit cards, UPI, Net Banking, and popular wallets. If you're facing issues, try clearing your cache or using a different browser.",
            "For payment issues, first check with your bank if the amount was deducted. If it was, the order may still be processing — wait 24 hours before reaching out."
        ]
    },

    "account": {
        "patterns": [
            "account", "login", "sign in", "sign up", "register",
            "forgot password", "reset password", "can't login", "account locked",
            "create account", "my account", "profile"
        ],
        "responses": [
            "For login issues, try the 'Forgot Password' option on the login page. A reset link will be sent to your registered email within a few minutes.",
            "To create an account, click 'Sign Up' on our homepage and fill in your details. It takes less than a minute!",
            "If your account is locked, it's usually due to multiple failed login attempts. Wait 15 minutes and try again, or use 'Forgot Password' to reset."
        ]
    },

    "product": {
        "patterns": [
            "product", "item", "stock", "available", "out of stock",
            "product details", "specifications", "size", "color",
            "product not available", "when will it be available", "restock"
        ],
        "responses": [
            "You can find full product details including size, specs, and availability on the product page. Use the search bar to find specific items.",
            "If a product is out of stock, you can click 'Notify Me' on the product page and we'll email you when it's back.",
            "For product questions, check the product description and reviews on our website. Still have questions? Our team is happy to help!"
        ]
    },

    "shipping": {
        "patterns": [
            "shipping", "delivery", "how long", "delivery time",
            "fast delivery", "express shipping", "free shipping",
            "shipping cost", "shipping fee", "delivery charge",
            "international shipping", "ship to"
        ],
        "responses": [
            "Standard delivery takes 3-5 business days. Express shipping (1-2 days) is available at checkout for an additional fee. Orders above ₹999 get free standard shipping.",
            "We offer free standard shipping on orders over ₹999. Express delivery is available for ₹99 extra. International shipping takes 7-14 business days.",
            "Delivery timelines: Standard (3-5 days), Express (1-2 days). You'll receive a tracking link via email once your order ships."
        ]
    },

    "contact": {
        "patterns": [
            "contact", "speak to agent", "human", "real person",
            "customer service", "support team", "email support",
            "phone number", "call", "live chat", "help"
        ],
        "responses": [
            "You can reach our support team at support@store.com or call us at 1800-XXX-XXXX (Mon-Sat, 9am-6pm). Live chat is also available on our website.",
            "To speak with a human agent, click 'Live Chat' on our website during business hours (9am-6pm, Mon-Sat), or email support@store.com.",
            "Our support team is available Monday to Saturday, 9am to 6pm. Email: support@store.com | Phone: 1800-XXX-XXXX"
        ]
    },

    "discount": {
        "patterns": [
            "discount", "coupon", "promo code", "offer", "sale",
            "deal", "voucher", "code", "cashback", "apply coupon"
        ],
        "responses": [
            "Check our 'Offers' page for current deals and promo codes. You can also subscribe to our newsletter to get exclusive discounts!",
            "To apply a coupon, add items to your cart and enter the code at checkout. If a code isn't working, check the expiry date and terms.",
            "We run seasonal sales and send exclusive promo codes to newsletter subscribers. Sign up on our homepage to never miss a deal!"
        ]
    },

    "fallback": {
        "patterns": [],
        "responses": [
            "I'm not sure I understood that. Could you rephrase your question?",
            "Hmm, I didn't quite catch that. Try asking about orders, refunds, shipping, payments, or account issues.",
            "I'm still learning! For complex queries, please contact our support team at support@store.com."
        ]
    }
}