import streamlit as st
import pandas as pd
import json
import hashlib
from datetime import datetime
import os

# Page configuration
st.set_page_config(
    page_title="BookStore - Your Online Book Shop",
    page_icon="📚",
    layout="wide"
)

# Initialize session state
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'username' not in st.session_state:
    st.session_state.username = None
if 'is_admin' not in st.session_state:
    st.session_state.is_admin = False
if 'cart' not in st.session_state:
    st.session_state.cart = []

# File paths for data storage
USERS_FILE = 'users.json'
BOOKS_FILE = 'books.json'
ORDERS_FILE = 'orders.json'

# Helper functions for data management
def load_json(filename, default):
    """Load JSON data from file"""
    if os.path.exists(filename):
        try:
            with open(filename, 'r') as f:
                return json.load(f)
        except:
            return default
    return default

def save_json(filename, data):
    """Save data to JSON file"""
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)

def hash_password(password):
    """Hash password using SHA-256"""
    return hashlib.sha256(password.encode()).hexdigest()

def initialize_data():
    """Initialize default data if files don't exist"""
    # Initialize users
    users = load_json(USERS_FILE, {})
    if not users:
        users = {
            'admin': {
                'password': hash_password('admin123'),
                'email': 'admin@bookstore.com',
                'is_admin': True
            }
        }
        save_json(USERS_FILE, users)
    
    # Initialize books
    books = load_json(BOOKS_FILE, [])
    if not books:
        books = [
            # Fiction
            {'id': 1, 'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'price': 12.99, 'category': 'Fiction', 'description': 'A classic American novel set in the Jazz Age, exploring themes of wealth and love.', 'stock': 50, 'image': '📕'},
            {'id': 2, 'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'price': 14.99, 'category': 'Fiction', 'description': 'A gripping tale of racial injustice and childhood innocence in the Deep South.', 'stock': 45, 'image': '📗'},
            {'id': 3, 'title': 'The Catcher in the Rye', 'author': 'J.D. Salinger', 'price': 13.49, 'category': 'Fiction', 'description': 'A story about teenage rebellion and alienation in post-war America.', 'stock': 38, 'image': '📕'},
            {'id': 4, 'title': 'Beloved', 'author': 'Toni Morrison', 'price': 15.99, 'category': 'Fiction', 'description': 'A powerful novel about the lasting effects of slavery.', 'stock': 42, 'image': '📗'},
            {'id': 5, 'title': 'The Road', 'author': 'Cormac McCarthy', 'price': 14.49, 'category': 'Fiction', 'description': 'A post-apocalyptic tale of a father and son journey.', 'stock': 35, 'image': '📘'},
            
            # Science Fiction
            {'id': 6, 'title': '1984', 'author': 'George Orwell', 'price': 13.99, 'category': 'Science Fiction', 'description': 'A dystopian social science fiction novel about totalitarianism.', 'stock': 60, 'image': '📘'},
            {'id': 7, 'title': 'Dune', 'author': 'Frank Herbert', 'price': 18.99, 'category': 'Science Fiction', 'description': 'Epic science fiction novel set on the desert planet Arrakis.', 'stock': 52, 'image': '📙'},
            {'id': 8, 'title': 'Neuromancer', 'author': 'William Gibson', 'price': 14.99, 'category': 'Science Fiction', 'description': 'Groundbreaking cyberpunk novel about artificial intelligence.', 'stock': 44, 'image': '📘'},
            {'id': 9, 'title': 'The Left Hand of Darkness', 'author': 'Ursula K. Le Guin', 'price': 13.99, 'category': 'Science Fiction', 'description': 'Science fiction exploring gender and society on an alien world.', 'stock': 40, 'image': '📗'},
            {'id': 10, 'title': 'Foundation', 'author': 'Isaac Asimov', 'price': 15.49, 'category': 'Science Fiction', 'description': 'Classic saga about the fall and rise of galactic civilizations.', 'stock': 48, 'image': '📙'},
            
            # Fantasy
            {'id': 11, 'title': 'The Hobbit', 'author': 'J.R.R. Tolkien', 'price': 15.99, 'category': 'Fantasy', 'description': 'A fantasy adventure of Bilbo Baggins and his quest for treasure.', 'stock': 55, 'image': '📚'},
            {'id': 12, 'title': 'Harry Potter and the Sorcerer\'s Stone', 'author': 'J.K. Rowling', 'price': 16.99, 'category': 'Fantasy', 'description': 'First book in the beloved Harry Potter series.', 'stock': 65, 'image': '📕'},
            {'id': 13, 'title': 'The Name of the Wind', 'author': 'Patrick Rothfuss', 'price': 17.99, 'category': 'Fantasy', 'description': 'Epic fantasy about a legendary hero telling his life story.', 'stock': 43, 'image': '📗'},
            {'id': 14, 'title': 'A Game of Thrones', 'author': 'George R.R. Martin', 'price': 18.99, 'category': 'Fantasy', 'description': 'First book of A Song of Ice and Fire, epic political fantasy.', 'stock': 58, 'image': '📘'},
            {'id': 15, 'title': 'The Way of Kings', 'author': 'Brandon Sanderson', 'price': 19.99, 'category': 'Fantasy', 'description': 'Epic fantasy with unique magic system and complex world-building.', 'stock': 47, 'image': '📙'},
            
            # Mystery & Thriller
            {'id': 16, 'title': 'The Girl with the Dragon Tattoo', 'author': 'Stieg Larsson', 'price': 15.99, 'category': 'Mystery', 'description': 'Gripping Swedish mystery thriller about corruption and murder.', 'stock': 51, 'image': '📕'},
            {'id': 17, 'title': 'Gone Girl', 'author': 'Gillian Flynn', 'price': 14.99, 'category': 'Mystery', 'description': 'Psychological thriller about a marriage gone terribly wrong.', 'stock': 46, 'image': '📗'},
            {'id': 18, 'title': 'The Da Vinci Code', 'author': 'Dan Brown', 'price': 16.49, 'category': 'Mystery', 'description': 'Mystery thriller involving art, religion, and conspiracy.', 'stock': 54, 'image': '📘'},
            {'id': 19, 'title': 'Big Little Lies', 'author': 'Liane Moriarty', 'price': 13.99, 'category': 'Mystery', 'description': 'Mystery centered around three mothers and a school murder.', 'stock': 41, 'image': '📙'},
            {'id': 20, 'title': 'The Silent Patient', 'author': 'Alex Michaelides', 'price': 14.99, 'category': 'Mystery', 'description': 'Psychological thriller about a woman who stops speaking.', 'stock': 49, 'image': '📕'},
            
            # Romance
            {'id': 21, 'title': 'Pride and Prejudice', 'author': 'Jane Austen', 'price': 11.99, 'category': 'Romance', 'description': 'Classic romantic novel about Elizabeth Bennet and Mr. Darcy.', 'stock': 40, 'image': '📙'},
            {'id': 22, 'title': 'Outlander', 'author': 'Diana Gabaldon', 'price': 17.99, 'category': 'Romance', 'description': 'Time-travel romance set in 18th century Scotland.', 'stock': 45, 'image': '📗'},
            {'id': 23, 'title': 'The Notebook', 'author': 'Nicholas Sparks', 'price': 12.99, 'category': 'Romance', 'description': 'Heartwarming love story spanning decades.', 'stock': 52, 'image': '📕'},
            {'id': 24, 'title': 'Me Before You', 'author': 'Jojo Moyes', 'price': 13.99, 'category': 'Romance', 'description': 'Emotional romance about love and life choices.', 'stock': 48, 'image': '📘'},
            {'id': 25, 'title': 'The Hating Game', 'author': 'Sally Thorne', 'price': 12.49, 'category': 'Romance', 'description': 'Enemies-to-lovers workplace romance with wit and charm.', 'stock': 44, 'image': '📙'},
            
            # Non-Fiction
            {'id': 26, 'title': 'Sapiens', 'author': 'Yuval Noah Harari', 'price': 18.99, 'category': 'Non-Fiction', 'description': 'A brief history of humankind from Stone Age to modern times.', 'stock': 62, 'image': '📚'},
            {'id': 27, 'title': 'Educated', 'author': 'Tara Westover', 'price': 16.99, 'category': 'Non-Fiction', 'description': 'Memoir about growing up in an isolated family and self-education.', 'stock': 56, 'image': '📕'},
            {'id': 28, 'title': 'Thinking, Fast and Slow', 'author': 'Daniel Kahneman', 'price': 17.99, 'category': 'Non-Fiction', 'description': 'Exploration of the two systems that drive human thinking.', 'stock': 47, 'image': '📗'},
            {'id': 29, 'title': 'The Immortal Life of Henrietta Lacks', 'author': 'Rebecca Skloot', 'price': 15.99, 'category': 'Non-Fiction', 'description': 'True story of the woman behind revolutionary medical cells.', 'stock': 43, 'image': '📘'},
            {'id': 30, 'title': 'Atomic Habits', 'author': 'James Clear', 'price': 16.99, 'category': 'Non-Fiction', 'description': 'Guide to building good habits and breaking bad ones.', 'stock': 68, 'image': '📙'},
            
            # Biography
            {'id': 31, 'title': 'Steve Jobs', 'author': 'Walter Isaacson', 'price': 19.99, 'category': 'Biography', 'description': 'Authorized biography of the Apple co-founder.', 'stock': 50, 'image': '📚'},
            {'id': 32, 'title': 'Becoming', 'author': 'Michelle Obama', 'price': 18.99, 'category': 'Biography', 'description': 'Memoir by the former First Lady of the United States.', 'stock': 64, 'image': '📕'},
            {'id': 33, 'title': 'The Diary of a Young Girl', 'author': 'Anne Frank', 'price': 12.99, 'category': 'Biography', 'description': 'Powerful diary of a Jewish girl during the Holocaust.', 'stock': 55, 'image': '📗'},
            {'id': 34, 'title': 'Long Walk to Freedom', 'author': 'Nelson Mandela', 'price': 17.99, 'category': 'Biography', 'description': 'Autobiography of South African anti-apartheid leader.', 'stock': 42, 'image': '📘'},
            {'id': 35, 'title': 'Born a Crime', 'author': 'Trevor Noah', 'price': 15.99, 'category': 'Biography', 'description': 'Memoir of growing up in South Africa during apartheid.', 'stock': 53, 'image': '📙'},
            
            # History
            {'id': 36, 'title': 'A People\'s History of the United States', 'author': 'Howard Zinn', 'price': 18.99, 'category': 'History', 'description': 'American history from the perspective of ordinary people.', 'stock': 45, 'image': '📚'},
            {'id': 37, 'title': 'Guns, Germs, and Steel', 'author': 'Jared Diamond', 'price': 17.99, 'category': 'History', 'description': 'Exploration of why civilizations developed differently.', 'stock': 48, 'image': '📕'},
            {'id': 38, 'title': 'The Silk Roads', 'author': 'Peter Frankopan', 'price': 19.99, 'category': 'History', 'description': 'New history of the world from the perspective of the East.', 'stock': 41, 'image': '📗'},
            {'id': 39, 'title': 'SPQR', 'author': 'Mary Beard', 'price': 18.49, 'category': 'History', 'description': 'Comprehensive history of Ancient Rome.', 'stock': 39, 'image': '📘'},
            {'id': 40, 'title': 'Team of Rivals', 'author': 'Doris Kearns Goodwin', 'price': 19.99, 'category': 'History', 'description': 'Political genius of Abraham Lincoln and his cabinet.', 'stock': 44, 'image': '📙'},
            
            # Self-Help
            {'id': 41, 'title': 'The 7 Habits of Highly Effective People', 'author': 'Stephen Covey', 'price': 16.99, 'category': 'Self-Help', 'description': 'Timeless principles for personal and professional effectiveness.', 'stock': 70, 'image': '📚'},
            {'id': 42, 'title': 'How to Win Friends and Influence People', 'author': 'Dale Carnegie', 'price': 14.99, 'category': 'Self-Help', 'description': 'Classic guide to better relationships and communication.', 'stock': 65, 'image': '📕'},
            {'id': 43, 'title': 'The Power of Now', 'author': 'Eckhart Tolle', 'price': 15.99, 'category': 'Self-Help', 'description': 'Guide to spiritual enlightenment and living in the present.', 'stock': 58, 'image': '📗'},
            {'id': 44, 'title': 'Daring Greatly', 'author': 'Brené Brown', 'price': 16.49, 'category': 'Self-Help', 'description': 'Exploration of vulnerability and courage in daily life.', 'stock': 54, 'image': '📘'},
            {'id': 45, 'title': 'The Subtle Art of Not Giving a F*ck', 'author': 'Mark Manson', 'price': 15.49, 'category': 'Self-Help', 'description': 'Counterintuitive approach to living a good life.', 'stock': 62, 'image': '📙'},
            
            # Children's Books
            {'id': 46, 'title': 'Where the Wild Things Are', 'author': 'Maurice Sendak', 'price': 9.99, 'category': 'Children', 'description': 'Classic children\'s picture book about imagination.', 'stock': 75, 'image': '📕'},
            {'id': 47, 'title': 'The Very Hungry Caterpillar', 'author': 'Eric Carle', 'price': 8.99, 'category': 'Children', 'description': 'Beloved children\'s book about a caterpillar\'s transformation.', 'stock': 80, 'image': '📗'},
            {'id': 48, 'title': 'Charlotte\'s Web', 'author': 'E.B. White', 'price': 11.99, 'category': 'Children', 'description': 'Heartwarming story of friendship between a pig and spider.', 'stock': 68, 'image': '📘'},
            {'id': 49, 'title': 'Matilda', 'author': 'Roald Dahl', 'price': 12.99, 'category': 'Children', 'description': 'Story of a brilliant young girl with telekinetic powers.', 'stock': 72, 'image': '📙'},
            {'id': 50, 'title': 'The Giving Tree', 'author': 'Shel Silverstein', 'price': 10.99, 'category': 'Children', 'description': 'Touching story about selfless love and giving.', 'stock': 70, 'image': '📚'}
        ]
        save_json(BOOKS_FILE, books)
    
    # Initialize orders
    if not os.path.exists(ORDERS_FILE):
        save_json(ORDERS_FILE, [])

# Authentication functions
def register_user(username, password, email):
    """Register a new user"""
    users = load_json(USERS_FILE, {})
    
    if username in users:
        return False, "Username already exists"
    
    users[username] = {
        'password': hash_password(password),
        'email': email,
        'is_admin': False
    }
    save_json(USERS_FILE, users)
    return True, "Registration successful!"

def login_user(username, password):
    """Authenticate user"""
    users = load_json(USERS_FILE, {})
    
    if username not in users:
        return False, "User not found"
    
    if users[username]['password'] == hash_password(password):
        st.session_state.logged_in = True
        st.session_state.username = username
        st.session_state.is_admin = users[username].get('is_admin', False)
        return True, "Login successful!"
    
    return False, "Incorrect password"

def logout_user():
    """Logout current user"""
    st.session_state.logged_in = False
    st.session_state.username = None
    st.session_state.is_admin = False
    st.session_state.cart = []

# Book management functions
def get_books():
    """Get all books"""
    return load_json(BOOKS_FILE, [])

def add_book(book_data):
    """Add a new book"""
    books = get_books()
    new_id = max([b['id'] for b in books], default=0) + 1
    book_data['id'] = new_id
    books.append(book_data)
    save_json(BOOKS_FILE, books)
    return True

def update_book(book_id, book_data):
    """Update existing book"""
    books = get_books()
    for i, book in enumerate(books):
        if book['id'] == book_id:
            book_data['id'] = book_id
            books[i] = book_data
            save_json(BOOKS_FILE, books)
            return True
    return False

def delete_book(book_id):
    """Delete a book"""
    books = get_books()
    books = [b for b in books if b['id'] != book_id]
    save_json(BOOKS_FILE, books)
    return True

# Cart functions
def add_to_cart(book):
    """Add book to cart"""
    st.session_state.cart.append(book)

def remove_from_cart(index):
    """Remove book from cart"""
    if 0 <= index < len(st.session_state.cart):
        st.session_state.cart.pop(index)

def clear_cart():
    """Clear shopping cart"""
    st.session_state.cart = []

def place_order():
    """Place an order with validation"""
    if not st.session_state.cart:
        return False, "Cart is empty"
    
    try:
        orders = load_json(ORDERS_FILE, [])
        
        # Calculate totals
        subtotal = sum(item['price'] for item in st.session_state.cart)
        tax = subtotal * 0.08
        shipping = 5.99 if subtotal < 50 else 0
        total = subtotal + tax + shipping
        
        order = {
            'order_id': len(orders) + 1,
            'username': st.session_state.username,
            'items': st.session_state.cart.copy(),
            'subtotal': round(subtotal, 2),
            'tax': round(tax, 2),
            'shipping': round(shipping, 2),
            'total': round(total, 2),
            'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'status': 'Pending'
        }
        orders.append(order)
        save_json(ORDERS_FILE, orders)
        
        # Update inventory
        books = get_books()
        cart_items = {}
        for item in st.session_state.cart:
            cart_items[item['id']] = cart_items.get(item['id'], 0) + 1
        
        for book in books:
            if book['id'] in cart_items:
                book['stock'] = max(0, book['stock'] - cart_items[book['id']])
        
        save_json(BOOKS_FILE, books)
        
        clear_cart()
        return True, f"Order #{order['order_id']} placed successfully!"
    except Exception as e:
        return False, f"Error placing order: {str(e)}"

# Page functions
def show_login_page():
    """Display sleek and professional login/register page"""
    
    # Custom CSS for professional styling
    st.markdown("""
        <style>
        .main-header {
            text-align: center;
            padding: 2rem 0;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border-radius: 10px;
            margin-bottom: 2rem;
        }
        .main-header h1 {
            font-size: 3rem;
            margin: 0;
            font-weight: 700;
        }
        .main-header p {
            font-size: 1.2rem;
            margin: 0.5rem 0 0 0;
            opacity: 0.9;
        }
        .login-container {
            max-width: 500px;
            margin: 0 auto;
            padding: 2rem;
            background: white;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        .stButton>button {
            width: 100%;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            padding: 0.75rem;
            font-size: 1.1rem;
            font-weight: 600;
            border-radius: 5px;
            margin-top: 1rem;
        }
        .stButton>button:hover {
            background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }
        .feature-box {
            background: #f8f9fa;
            padding: 1.5rem;
            border-radius: 8px;
            margin: 1rem 0;
            border-left: 4px solid #667eea;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Header
    st.markdown("""
        <div class="main-header">
            <h1>📚 BookStore</h1>
            <p>Your Premium Online Book Shop</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Two column layout for features
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
            <div class="feature-box">
                <h3 style="margin:0;">📖 50+ Books</h3>
                <p style="margin:0.5rem 0 0 0; font-size:0.9rem;">Curated collection across all genres</p>
            </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
            <div class="feature-box">
                <h3 style="margin:0;">🚚 Fast Delivery</h3>
                <p style="margin:0.5rem 0 0 0; font-size:0.9rem;">Quick and secure shipping</p>
            </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
            <div class="feature-box">
                <h3 style="margin:0;">💳 Secure Payment</h3>
                <p style="margin:0.5rem 0 0 0; font-size:0.9rem;">Safe and encrypted checkout</p>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Login/Register tabs
    tab1, tab2 = st.tabs(["🔐 Login", "✨ Create Account"])
    
    with tab1:
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.markdown("### Welcome Back!")
            st.markdown("Sign in to continue shopping")
            
            with st.form("login_form", clear_on_submit=False):
                username = st.text_input("Username", placeholder="Enter your username", key="login_username")
                password = st.text_input("Password", type="password", placeholder="Enter your password", key="login_password")
                
                col_a, col_b = st.columns([1, 1])
                with col_a:
                    remember = st.checkbox("Remember me")
                with col_b:
                    st.markdown("<p style='text-align: right; margin-top: 0.5rem;'><a href='#'>Forgot password?</a></p>", unsafe_allow_html=True)
                
                submit = st.form_submit_button("Sign In", use_container_width=True)
                
                if submit:
                    if not username or not password:
                        st.error("⚠️ Please fill in all fields")
                    else:
                        success, message = login_user(username, password)
                        if success:
                            st.success("✅ " + message)
                            st.balloons()
                            st.rerun()
                        else:
                            st.error("❌ " + message)
            
            st.markdown("<br>", unsafe_allow_html=True)
            st.info("💡 **Demo Account**\n\nUsername: `admin`\n\nPassword: `admin123`")
    
    with tab2:
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.markdown("### Join BookStore Today!")
            st.markdown("Create your account and start exploring")
            
            with st.form("register_form", clear_on_submit=True):
                new_username = st.text_input("Username", placeholder="Choose a username", key="reg_username")
                new_email = st.text_input("Email", placeholder="your.email@example.com", key="reg_email")
                new_password = st.text_input("Password", type="password", placeholder="Minimum 6 characters", key="reg_password")
                confirm_password = st.text_input("Confirm Password", type="password", placeholder="Re-enter password", key="reg_confirm")
                
                terms = st.checkbox("I agree to the Terms of Service and Privacy Policy")
                
                submit_register = st.form_submit_button("Create Account", use_container_width=True)
                
                if submit_register:
                    if not all([new_username, new_email, new_password, confirm_password]):
                        st.error("⚠️ Please fill in all fields")
                    elif not terms:
                        st.error("⚠️ Please accept the Terms of Service")
                    elif new_password != confirm_password:
                        st.error("❌ Passwords do not match")
                    elif len(new_password) < 6:
                        st.error("❌ Password must be at least 6 characters")
                    elif '@' not in new_email:
                        st.error("❌ Please enter a valid email address")
                    else:
                        success, message = register_user(new_username, new_password, new_email)
                        if success:
                            st.success("✅ " + message + " You can now login!")
                            st.balloons()
                        else:
                            st.error("❌ " + message)
            
            st.markdown("<br>", unsafe_allow_html=True)
            st.success("🎉 **Join 1000+ happy readers** who trust BookStore for their reading needs!")

def show_book_catalog():
    """Display professional book catalog with advanced features"""
    
    # Initialize pagination in session state
    if 'catalog_page' not in st.session_state:
        st.session_state.catalog_page = 0
    
    st.markdown("## 📖 Discover Your Next Great Read")
    
    books = get_books()
    
    # Advanced filters in columns
    col1, col2, col3, col4 = st.columns([3, 2, 2, 2])
    with col1:
        search_query = st.text_input("🔍 Search by title or author", "", key="search_books")
    with col2:
        categories = sorted(list(set([book['category'] for book in books])))
        selected_category = st.selectbox("📚 Category", ["All Categories"] + categories, key="filter_category")
    with col3:
        sort_options = {
            "Title (A-Z)": ("title", False),
            "Title (Z-A)": ("title", True),
            "Price (Low to High)": ("price", False),
            "Price (High to Low)": ("price", True),
            "Author (A-Z)": ("author", False),
        }
        sort_selection = st.selectbox("🔄 Sort by", list(sort_options.keys()), key="sort_books")
    with col4:
        price_filter = st.selectbox("💵 Price Range", ["All Prices", "Under $15", "$15-$20", "Over $20"], key="price_range")
    
    # Filter books
    filtered_books = books
    
    # Search filter
    if search_query:
        filtered_books = [b for b in filtered_books if 
                         search_query.lower() in b['title'].lower() or 
                         search_query.lower() in b['author'].lower()]
    
    # Category filter
    if selected_category != "All Categories":
        filtered_books = [b for b in filtered_books if b['category'] == selected_category]
    
    # Price filter
    if price_filter == "Under $15":
        filtered_books = [b for b in filtered_books if b['price'] < 15]
    elif price_filter == "$15-$20":
        filtered_books = [b for b in filtered_books if 15 <= b['price'] <= 20]
    elif price_filter == "Over $20":
        filtered_books = [b for b in filtered_books if b['price'] > 20]
    
    # Sort books
    sort_field, reverse = sort_options[sort_selection]
    filtered_books = sorted(filtered_books, key=lambda x: x[sort_field], reverse=reverse)
    
    # Show results count
    st.markdown(f"### Found {len(filtered_books)} books")
    
    if not filtered_books:
        st.warning("😕 No books found matching your criteria. Try adjusting your filters.")
        return
    
    # Pagination
    books_per_page = 12
    total_pages = (len(filtered_books) + books_per_page - 1) // books_per_page
    
    # Ensure current page is valid
    if st.session_state.catalog_page >= total_pages:
        st.session_state.catalog_page = 0
    
    start_idx = st.session_state.catalog_page * books_per_page
    end_idx = min(start_idx + books_per_page, len(filtered_books))
    current_books = filtered_books[start_idx:end_idx]
    
    # Display books in grid (4 columns)
    cols_per_row = 4
    for i in range(0, len(current_books), cols_per_row):
        cols = st.columns(cols_per_row)
        for j, col in enumerate(cols):
            if i + j < len(current_books):
                book = current_books[i + j]
                with col:
                    # Book card with styling
                    st.markdown(f"""
                        <div style="background: white; padding: 1rem; border-radius: 8px; 
                                    box-shadow: 0 2px 4px rgba(0,0,0,0.1); height: 100%; 
                                    border: 1px solid #e0e0e0;">
                            <div style="font-size: 3rem; text-align: center; margin-bottom: 0.5rem;">
                                {book['image']}
                            </div>
                            <h4 style="margin: 0; height: 2.5rem; overflow: hidden; text-overflow: ellipsis;">
                                {book['title']}
                            </h4>
                            <p style="margin: 0.3rem 0; color: #666; font-size: 0.9rem;">
                                by {book['author']}
                            </p>
                            <div style="background: #f0f0f0; padding: 0.3rem 0.6rem; border-radius: 4px; 
                                        display: inline-block; font-size: 0.85rem; margin: 0.5rem 0;">
                                {book['category']}
                            </div>
                            <p style="margin: 0.5rem 0; font-size: 1.3rem; font-weight: bold; color: #667eea;">
                                ${book['price']:.2f}
                            </p>
                            <p style="margin: 0.3rem 0; font-size: 0.85rem; color: {'#28a745' if book['stock'] > 20 else '#ffc107' if book['stock'] > 0 else '#dc3545'};">
                                {'✅ In Stock' if book['stock'] > 20 else f'⚠️ Only {book["stock"]} left' if book['stock'] > 0 else '❌ Out of Stock'}
                            </p>
                        </div>
                    """, unsafe_allow_html=True)
                    
                    with st.expander("📄 Details"):
                        st.write(book['description'])
                        st.write(f"**Available:** {book['stock']} copies")
                    
                    if book['stock'] > 0:
                        if st.button("🛒 Add to Cart", key=f"add_{book['id']}", use_container_width=True):
                            add_to_cart(book)
                            st.success(f"✅ Added to cart!")
                            st.rerun()
                    else:
                        st.button("❌ Out of Stock", key=f"oos_{book['id']}", disabled=True, use_container_width=True)
    
    # Pagination controls
    if total_pages > 1:
        st.markdown("<br>", unsafe_allow_html=True)
        col1, col2, col3, col4, col5 = st.columns([1, 1, 2, 1, 1])
        
        with col1:
            if st.button("⏮️ First", disabled=(st.session_state.catalog_page == 0)):
                st.session_state.catalog_page = 0
                st.rerun()
        
        with col2:
            if st.button("◀️ Previous", disabled=(st.session_state.catalog_page == 0)):
                st.session_state.catalog_page -= 1
                st.rerun()
        
        with col3:
            st.markdown(f"<p style='text-align: center; padding-top: 0.5rem;'><strong>Page {st.session_state.catalog_page + 1} of {total_pages}</strong></p>", unsafe_allow_html=True)
        
        with col4:
            if st.button("Next ▶️", disabled=(st.session_state.catalog_page >= total_pages - 1)):
                st.session_state.catalog_page += 1
                st.rerun()
        
        with col5:
            if st.button("Last ⏭️", disabled=(st.session_state.catalog_page >= total_pages - 1)):
                st.session_state.catalog_page = total_pages - 1
                st.rerun()

def show_cart():
    """Display professional shopping cart"""
    st.markdown("## 🛒 Your Shopping Cart")
    
    if not st.session_state.cart:
        st.markdown("""
            <div style="text-align: center; padding: 3rem; background: #f8f9fa; border-radius: 10px;">
                <h2 style="color: #666;">🛒 Your cart is empty</h2>
                <p style="font-size: 1.1rem; color: #888;">Start adding books to your cart to see them here!</p>
            </div>
        """, unsafe_allow_html=True)
        return
    
    # Group items by book id and count quantities
    cart_items = {}
    for item in st.session_state.cart:
        book_id = item['id']
        if book_id not in cart_items:
            cart_items[book_id] = {'item': item, 'quantity': 0}
        cart_items[book_id]['quantity'] += 1
    
    # Display cart items in a table-like format
    st.markdown("### Items in your cart")
    
    total = 0
    items_to_remove = []
    
    for book_id, data in cart_items.items():
        item = data['item']
        quantity = data['quantity']
        item_total = item['price'] * quantity
        total += item_total
        
        col1, col2, col3, col4, col5, col6 = st.columns([1, 3, 2, 1, 2, 1])
        
        with col1:
            st.markdown(f"<div style='font-size: 2.5rem; text-align: center;'>{item['image']}</div>", unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"**{item['title']}**")
            st.caption(f"by {item['author']}")
        
        with col3:
            st.write(f"**Category:** {item['category']}")
        
        with col4:
            st.markdown(f"<div style='text-align: center; font-size: 1.2rem;'>×{quantity}</div>", unsafe_allow_html=True)
        
        with col5:
            st.markdown(f"<div style='font-size: 1.3rem; font-weight: bold; color: #667eea;'>${item_total:.2f}</div>", unsafe_allow_html=True)
            st.caption(f"${item['price']:.2f} each")
        
        with col6:
            if st.button("🗑️", key=f"remove_{book_id}", help="Remove from cart"):
                # Remove all instances of this book
                items_to_remove.append(book_id)
        
        st.divider()
    
    # Remove items if needed
    if items_to_remove:
        st.session_state.cart = [item for item in st.session_state.cart if item['id'] not in items_to_remove]
        st.rerun()
    
    # Cart summary
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col2:
        st.markdown("""
            <div style="background: white; padding: 1.5rem; border-radius: 10px; 
                        box-shadow: 0 4px 6px rgba(0,0,0,0.1); border: 2px solid #667eea;">
                <h3 style="margin-top: 0;">Order Summary</h3>
        """, unsafe_allow_html=True)
        
        subtotal = total
        tax = total * 0.08  # 8% tax
        shipping = 5.99 if total < 50 else 0
        grand_total = subtotal + tax + shipping
        
        st.markdown(f"""
                <div style="margin: 1rem 0;">
                    <div style="display: flex; justify-content: space-between; margin: 0.5rem 0;">
                        <span>Subtotal:</span>
                        <span>${subtotal:.2f}</span>
                    </div>
                    <div style="display: flex; justify-content: space-between; margin: 0.5rem 0;">
                        <span>Tax (8%):</span>
                        <span>${tax:.2f}</span>
                    </div>
                    <div style="display: flex; justify-content: space-between; margin: 0.5rem 0;">
                        <span>Shipping:</span>
                        <span>{'FREE' if shipping == 0 else f'${shipping:.2f}'}</span>
                    </div>
                    <hr style="margin: 1rem 0;">
                    <div style="display: flex; justify-content: space-between; margin: 0.5rem 0; 
                                font-size: 1.3rem; font-weight: bold;">
                        <span>Total:</span>
                        <span style="color: #667eea;">${grand_total:.2f}</span>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        if total < 50:
            st.info(f"💡 Add ${50 - total:.2f} more for free shipping!")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        col_a, col_b = st.columns(2)
        with col_a:
            if st.button("🗑️ Clear Cart", use_container_width=True, type="secondary"):
                clear_cart()
                st.rerun()
        with col_b:
            if st.button("💳 Checkout", use_container_width=True, type="primary"):
                # Update cart with grand total for order
                success, message = place_order()
                if success:
                    st.success("✅ " + message)
                    st.balloons()
                    st.rerun()
                else:
                    st.error("❌ " + message)

def show_orders():
    """Display user orders with tracking"""
    st.markdown("## 📦 Your Order History")
    
    orders = load_json(ORDERS_FILE, [])
    user_orders = [o for o in orders if o['username'] == st.session_state.username]
    
    if not user_orders:
        st.markdown("""
            <div style="text-align: center; padding: 3rem; background: #f8f9fa; border-radius: 10px;">
                <h2 style="color: #666;">📦 No orders yet</h2>
                <p style="font-size: 1.1rem; color: #888;">Your order history will appear here once you make your first purchase!</p>
            </div>
        """, unsafe_allow_html=True)
        return
    
    # Order statistics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"""
            <div class="metric-card">
                <h3 style="margin: 0; color: #667eea;">{len(user_orders)}</h3>
                <p style="margin: 0.5rem 0 0 0; color: #666;">Total Orders</p>
            </div>
        """, unsafe_allow_html=True)
    with col2:
        total_spent = sum(o['total'] for o in user_orders)
        st.markdown(f"""
            <div class="metric-card">
                <h3 style="margin: 0; color: #667eea;">${total_spent:.2f}</h3>
                <p style="margin: 0.5rem 0 0 0; color: #666;">Total Spent</p>
            </div>
        """, unsafe_allow_html=True)
    with col3:
        total_items = sum(len(o['items']) for o in user_orders)
        st.markdown(f"""
            <div class="metric-card">
                <h3 style="margin: 0; color: #667eea;">{total_items}</h3>
                <p style="margin: 0.5rem 0 0 0; color: #666;">Books Purchased</p>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### Your Orders")
    
    # Display orders (most recent first)
    for order in reversed(user_orders):
        status_color = {
            'Pending': '#ffc107',
            'Processing': '#17a2b8',
            'Shipped': '#28a745',
            'Delivered': '#28a745',
            'Cancelled': '#dc3545'
        }.get(order['status'], '#666')
        
        with st.expander(f"Order #{order['order_id']} - {order['date']} - ${order['total']:.2f}", expanded=False):
            col1, col2 = st.columns([3, 1])
            
            with col1:
                st.markdown(f"""
                    <div style="background: {status_color}20; padding: 0.5rem 1rem; 
                                border-radius: 5px; display: inline-block; margin-bottom: 1rem;">
                        <strong style="color: {status_color};">● {order['status']}</strong>
                    </div>
                """, unsafe_allow_html=True)
                
                st.markdown("**Items:**")
                for item in order['items']:
                    st.write(f"• {item['title']} by {item['author']} - ${item['price']:.2f}")
            
            with col2:
                st.markdown(f"""
                    <div style="background: #f8f9fa; padding: 1rem; border-radius: 8px;">
                        <strong>Order Date</strong><br>
                        {order['date']}<br><br>
                        <strong>Total Amount</strong><br>
                        ${order['total']:.2f}
                    </div>
                """, unsafe_allow_html=True)

def show_admin_panel():
    """Display professional admin panel with analytics"""
    st.markdown("## ⚙️ Admin Dashboard")
    
    # Load data
    books = get_books()
    orders = load_json(ORDERS_FILE, [])
    users = load_json(USERS_FILE, {})
    
    # Key metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
            <div class="metric-card" style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white;">
                <h2 style="margin: 0;">{len(books)}</h2>
                <p style="margin: 0.5rem 0 0 0;">Total Books</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
            <div class="metric-card" style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); color: white;">
                <h2 style="margin: 0;">{len(orders)}</h2>
                <p style="margin: 0.5rem 0 0 0;">Total Orders</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        total_revenue = sum(order['total'] for order in orders)
        st.markdown(f"""
            <div class="metric-card" style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); color: white;">
                <h2 style="margin: 0;">${total_revenue:.2f}</h2>
                <p style="margin: 0.5rem 0 0 0;">Total Revenue</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
            <div class="metric-card" style="background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%); color: white;">
                <h2 style="margin: 0;">{len(users)}</h2>
                <p style="margin: 0.5rem 0 0 0;">Total Users</p>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Tab navigation for admin functions
    admin_tabs = st.tabs(["📚 Manage Books", "📦 View Orders", "📊 Analytics", "👥 Users"])
    
    with admin_tabs[0]:
        st.markdown("### 📚 Book Management")
        
        # Add new book
        with st.expander("➕ Add New Book", expanded=False):
            with st.form("add_book_form", clear_on_submit=True):
                col1, col2 = st.columns(2)
                with col1:
                    title = st.text_input("Title *")
                    author = st.text_input("Author *")
                    category = st.selectbox("Category *", ["Fiction", "Science Fiction", "Fantasy", 
                                                           "Mystery", "Romance", "Non-Fiction", 
                                                           "Biography", "History", "Self-Help", "Children"])
                with col2:
                    price = st.number_input("Price ($) *", min_value=0.0, step=0.01, value=14.99)
                    stock = st.number_input("Stock *", min_value=0, step=1, value=50)
                    image = st.text_input("Emoji Icon", value="📖")
                
                description = st.text_area("Description *", height=100)
                
                if st.form_submit_button("➕ Add Book", use_container_width=True):
                    if not all([title, author, category, description]):
                        st.error("⚠️ Please fill in all required fields")
                    else:
                        book_data = {
                            'title': title,
                            'author': author,
                            'price': price,
                            'category': category,
                            'description': description,
                            'stock': stock,
                            'image': image
                        }
                        add_book(book_data)
                        st.success("✅ Book added successfully!")
                        st.rerun()
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("### Existing Books")
        
        # Search and filter for books
        col1, col2 = st.columns([3, 2])
        with col1:
            search_admin = st.text_input("🔍 Search books", key="admin_search")
        with col2:
            filter_category = st.selectbox("Filter by category", ["All"] + sorted(list(set([b['category'] for b in books]))), key="admin_filter")
        
        # Filter books
        display_books = books
        if search_admin:
            display_books = [b for b in display_books if search_admin.lower() in b['title'].lower() or search_admin.lower() in b['author'].lower()]
        if filter_category != "All":
            display_books = [b for b in display_books if b['category'] == filter_category]
        
        # Display books
        for book in display_books:
            with st.expander(f"{book['image']} {book['title']} by {book['author']} (${book['price']:.2f})"):
                with st.form(f"edit_book_{book['id']}"):
                    col1, col2 = st.columns(2)
                    with col1:
                        title = st.text_input("Title", value=book['title'], key=f"title_{book['id']}")
                        author = st.text_input("Author", value=book['author'], key=f"author_{book['id']}")
                        category = st.selectbox("Category", ["Fiction", "Science Fiction", "Fantasy", 
                                                             "Mystery", "Romance", "Non-Fiction", 
                                                             "Biography", "History", "Self-Help", "Children"],
                                              index=["Fiction", "Science Fiction", "Fantasy", 
                                                     "Mystery", "Romance", "Non-Fiction", 
                                                     "Biography", "History", "Self-Help", "Children"].index(book['category']) if book['category'] in ["Fiction", "Science Fiction", "Fantasy", "Mystery", "Romance", "Non-Fiction", "Biography", "History", "Self-Help", "Children"] else 0,
                                              key=f"cat_{book['id']}")
                    with col2:
                        price = st.number_input("Price", value=book['price'], step=0.01, key=f"price_{book['id']}")
                        stock = st.number_input("Stock", value=book['stock'], step=1, key=f"stock_{book['id']}")
                        image = st.text_input("Emoji Icon", value=book['image'], key=f"img_{book['id']}")
                    
                    description = st.text_area("Description", value=book['description'], key=f"desc_{book['id']}")
                    
                    col_a, col_b, col_c = st.columns(3)
                    with col_a:
                        if st.form_submit_button("💾 Update", use_container_width=True):
                            book_data = {
                                'title': title,
                                'author': author,
                                'price': price,
                                'category': category,
                                'description': description,
                                'stock': stock,
                                'image': image
                            }
                            update_book(book['id'], book_data)
                            st.success("✅ Book updated!")
                            st.rerun()
                    with col_b:
                        pass
                    with col_c:
                        if st.form_submit_button("🗑️ Delete", use_container_width=True, type="secondary"):
                            delete_book(book['id'])
                            st.success("✅ Book deleted!")
                            st.rerun()
    
    with admin_tabs[1]:
        st.markdown("### 📦 All Orders")
        
        if not orders:
            st.info("No orders have been placed yet.")
        else:
            # Order filters
            col1, col2 = st.columns(2)
            with col1:
                status_filter = st.selectbox("Filter by status", ["All", "Pending", "Processing", "Shipped", "Delivered", "Cancelled"])
            with col2:
                sort_orders = st.selectbox("Sort by", ["Newest First", "Oldest First", "Highest Value", "Lowest Value"])
            
            # Filter and sort
            display_orders = orders
            if status_filter != "All":
                display_orders = [o for o in display_orders if o['status'] == status_filter]
            
            if sort_orders == "Newest First":
                display_orders = sorted(display_orders, key=lambda x: x['order_id'], reverse=True)
            elif sort_orders == "Oldest First":
                display_orders = sorted(display_orders, key=lambda x: x['order_id'])
            elif sort_orders == "Highest Value":
                display_orders = sorted(display_orders, key=lambda x: x['total'], reverse=True)
            else:
                display_orders = sorted(display_orders, key=lambda x: x['total'])
            
            for order in display_orders:
                status_color = {
                    'Pending': '#ffc107',
                    'Processing': '#17a2b8',
                    'Shipped': '#28a745',
                    'Delivered': '#28a745',
                    'Cancelled': '#dc3545'
                }.get(order['status'], '#666')
                
                with st.expander(f"Order #{order['order_id']} - {order['username']} - ${order['total']:.2f} - {order['status']}"):
                    col1, col2 = st.columns([2, 1])
                    
                    with col1:
                        st.write(f"**Customer:** {order['username']}")
                        st.write(f"**Date:** {order['date']}")
                        st.write(f"**Total:** ${order['total']:.2f}")
                        st.markdown(f"""
                            <div style="background: {status_color}20; padding: 0.5rem 1rem; 
                                        border-radius: 5px; display: inline-block; margin: 0.5rem 0;">
                                <strong style="color: {status_color};">Status: {order['status']}</strong>
                            </div>
                        """, unsafe_allow_html=True)
                        
                        st.markdown("**Items:**")
                        for item in order['items']:
                            st.write(f"• {item['title']} by {item['author']} - ${item['price']:.2f}")
                    
                    with col2:
                        st.write("**Update Status:**")
                        new_status = st.selectbox("", ["Pending", "Processing", "Shipped", "Delivered", "Cancelled"],
                                                 index=["Pending", "Processing", "Shipped", "Delivered", "Cancelled"].index(order['status']),
                                                 key=f"status_{order['order_id']}")
                        
                        if st.button("Update", key=f"update_{order['order_id']}"):
                            orders_list = load_json(ORDERS_FILE, [])
                            for o in orders_list:
                                if o['order_id'] == order['order_id']:
                                    o['status'] = new_status
                            save_json(ORDERS_FILE, orders_list)
                            st.success("✅ Status updated!")
                            st.rerun()
    
    with admin_tabs[2]:
        st.markdown("### 📊 Analytics & Insights")
        
        if orders:
            # Revenue over time (simplified)
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("#### 📈 Category Distribution")
                category_counts = {}
                for book in books:
                    category_counts[book['category']] = category_counts.get(book['category'], 0) + 1
                
                if category_counts:
                    st.bar_chart(category_counts)
            
            with col2:
                st.markdown("#### 💰 Top Selling Categories")
                category_revenue = {}
                for order in orders:
                    for item in order['items']:
                        cat = item.get('category', 'Unknown')
                        category_revenue[cat] = category_revenue.get(cat, 0) + item['price']
                
                if category_revenue:
                    sorted_revenue = dict(sorted(category_revenue.items(), key=lambda x: x[1], reverse=True))
                    for cat, rev in list(sorted_revenue.items())[:5]:
                        st.write(f"**{cat}:** ${rev:.2f}")
            
            # Inventory alerts
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown("#### ⚠️ Inventory Alerts")
            low_stock = [b for b in books if b['stock'] < 20]
            if low_stock:
                for book in low_stock:
                    st.warning(f"📚 **{book['title']}** - Only {book['stock']} left in stock")
            else:
                st.success("✅ All books are well stocked!")
        
        else:
            st.info("No data available yet. Analytics will appear once orders are placed.")
    
    with admin_tabs[3]:
        st.markdown("### 👥 User Management")
        
        st.write(f"**Total Registered Users:** {len(users)}")
        
        for username, data in users.items():
            with st.expander(f"👤 {username} {'🔑 (Admin)' if data.get('is_admin', False) else ''}"):
                st.write(f"**Email:** {data.get('email', 'N/A')}")
                st.write(f"**Account Type:** {'Administrator' if data.get('is_admin', False) else 'Customer'}")
                
                # User's order history
                user_orders = [o for o in orders if o['username'] == username]
                st.write(f"**Total Orders:** {len(user_orders)}")
                if user_orders:
                    total_spent = sum(o['total'] for o in user_orders)
                    st.write(f"**Total Spent:** ${total_spent:.2f}")

# Main app
def main():
    # Initialize data
    initialize_data()
    
    # Show login page if not logged in
    if not st.session_state.logged_in:
        show_login_page()
        return
    
    # Custom CSS for professional styling
    st.markdown("""
        <style>
        .header-container {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 1.5rem;
            border-radius: 10px;
            margin-bottom: 1rem;
            color: white;
        }
        .user-info {
            background: rgba(255, 255, 255, 0.2);
            padding: 0.5rem 1rem;
            border-radius: 5px;
            display: inline-block;
        }
        .cart-summary {
            background: #f8f9fa;
            padding: 1rem;
            border-radius: 8px;
            border-left: 4px solid #667eea;
            margin: 1rem 0;
        }
        .stTabs [data-baseweb="tab-list"] {
            gap: 2rem;
            background-color: #f8f9fa;
            padding: 0.5rem 1rem;
            border-radius: 10px;
        }
        .stTabs [data-baseweb="tab"] {
            padding: 1rem 2rem;
            font-weight: 600;
            font-size: 1.1rem;
        }
        .stTabs [aria-selected="true"] {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white !important;
            border-radius: 5px;
        }
        .metric-card {
            background: white;
            padding: 1.5rem;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            text-align: center;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Header with user info
    col1, col2, col3 = st.columns([2, 2, 1])
    with col1:
        st.markdown(f"""
            <div class="header-container">
                <h1 style="margin: 0;">📚 BookStore</h1>
                <p style="margin: 0.5rem 0 0 0; opacity: 0.9;">Your Premium Online Book Shop</p>
            </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("<div style='padding-top: 1.5rem;'></div>", unsafe_allow_html=True)
        st.markdown(f"""
            <div class="user-info">
                <strong>👤 {st.session_state.username}</strong>
                {'<span style="margin-left: 1rem; background: rgba(255, 215, 0, 0.3); padding: 0.2rem 0.5rem; border-radius: 3px;">🔑 Admin</span>' if st.session_state.is_admin else ''}
            </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("<div style='padding-top: 2rem;'></div>", unsafe_allow_html=True)
        if st.button("🚪 Logout", use_container_width=True):
            logout_user()
            st.rerun()
    
    # Cart summary at top
    cart_count = len(st.session_state.cart)
    cart_total = sum(item['price'] for item in st.session_state.cart)
    
    if cart_count > 0:
        st.markdown(f"""
            <div class="cart-summary">
                <span style="font-size: 1.2rem;">🛒 <strong>{cart_count}</strong> items in cart | </span>
                <span style="font-size: 1.2rem;">💰 Total: <strong>${cart_total:.2f}</strong></span>
            </div>
        """, unsafe_allow_html=True)
    
    # Tab-based navigation
    if st.session_state.is_admin:
        tabs = st.tabs(["📖 Browse Books", "🛒 Shopping Cart", "📦 My Orders", "⚙️ Admin Panel"])
        
        with tabs[0]:
            show_book_catalog()
        
        with tabs[1]:
            show_cart()
        
        with tabs[2]:
            show_orders()
        
        with tabs[3]:
            show_admin_panel()
    else:
        tabs = st.tabs(["📖 Browse Books", "🛒 Shopping Cart", "📦 My Orders"])
        
        with tabs[0]:
            show_book_catalog()
        
        with tabs[1]:
            show_cart()
        
        with tabs[2]:
            show_orders()

if __name__ == "__main__":
    main()
