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
            {
                'id': 1,
                'title': 'The Great Gatsby',
                'author': 'F. Scott Fitzgerald',
                'price': 12.99,
                'category': 'Fiction',
                'description': 'A classic American novel set in the Jazz Age.',
                'stock': 50,
                'image': '📕'
            },
            {
                'id': 2,
                'title': 'To Kill a Mockingbird',
                'author': 'Harper Lee',
                'price': 14.99,
                'category': 'Fiction',
                'description': 'A gripping tale of racial injustice and childhood innocence.',
                'stock': 45,
                'image': '📗'
            },
            {
                'id': 3,
                'title': '1984',
                'author': 'George Orwell',
                'price': 13.99,
                'category': 'Science Fiction',
                'description': 'A dystopian social science fiction novel.',
                'stock': 60,
                'image': '📘'
            },
            {
                'id': 4,
                'title': 'Pride and Prejudice',
                'author': 'Jane Austen',
                'price': 11.99,
                'category': 'Romance',
                'description': 'A romantic novel of manners.',
                'stock': 40,
                'image': '📙'
            },
            {
                'id': 5,
                'title': 'The Hobbit',
                'author': 'J.R.R. Tolkien',
                'price': 15.99,
                'category': 'Fantasy',
                'description': 'A fantasy novel and children\'s book.',
                'stock': 55,
                'image': '📚'
            }
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
    """Place an order"""
    if not st.session_state.cart:
        return False, "Cart is empty"
    
    orders = load_json(ORDERS_FILE, [])
    order = {
        'order_id': len(orders) + 1,
        'username': st.session_state.username,
        'items': st.session_state.cart.copy(),
        'total': sum(item['price'] for item in st.session_state.cart),
        'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'status': 'Pending'
    }
    orders.append(order)
    save_json(ORDERS_FILE, orders)
    clear_cart()
    return True, f"Order #{order['order_id']} placed successfully!"

# Page functions
def show_login_page():
    """Display login/register page"""
    st.title("📚 BookStore - Your Online Book Shop")
    
    tab1, tab2 = st.tabs(["Login", "Register"])
    
    with tab1:
        st.subheader("Login to Your Account")
        with st.form("login_form"):
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            submit = st.form_submit_button("Login")
            
            if submit:
                success, message = login_user(username, password)
                if success:
                    st.success(message)
                    st.rerun()
                else:
                    st.error(message)
        
        st.info("💡 Demo admin account: username=`admin`, password=`admin123`")
    
    with tab2:
        st.subheader("Create New Account")
        with st.form("register_form"):
            new_username = st.text_input("Username")
            new_email = st.text_input("Email")
            new_password = st.text_input("Password", type="password")
            confirm_password = st.text_input("Confirm Password", type="password")
            submit_register = st.form_submit_button("Register")
            
            if submit_register:
                if new_password != confirm_password:
                    st.error("Passwords do not match")
                elif len(new_password) < 6:
                    st.error("Password must be at least 6 characters")
                else:
                    success, message = register_user(new_username, new_password, new_email)
                    if success:
                        st.success(message)
                    else:
                        st.error(message)

def show_book_catalog():
    """Display book catalog"""
    st.title("📚 Book Catalog")
    
    books = get_books()
    
    # Filters
    col1, col2, col3 = st.columns([2, 2, 1])
    with col1:
        search_query = st.text_input("🔍 Search books", "")
    with col2:
        categories = list(set([book['category'] for book in books]))
        selected_category = st.selectbox("Category", ["All"] + categories)
    with col3:
        sort_by = st.selectbox("Sort by", ["Title", "Price", "Author"])
    
    # Filter books
    filtered_books = books
    if search_query:
        filtered_books = [b for b in filtered_books if 
                         search_query.lower() in b['title'].lower() or 
                         search_query.lower() in b['author'].lower()]
    if selected_category != "All":
        filtered_books = [b for b in filtered_books if b['category'] == selected_category]
    
    # Sort books
    if sort_by == "Title":
        filtered_books = sorted(filtered_books, key=lambda x: x['title'])
    elif sort_by == "Price":
        filtered_books = sorted(filtered_books, key=lambda x: x['price'])
    elif sort_by == "Author":
        filtered_books = sorted(filtered_books, key=lambda x: x['author'])
    
    # Display books in grid
    if not filtered_books:
        st.warning("No books found matching your criteria.")
    else:
        cols_per_row = 3
        for i in range(0, len(filtered_books), cols_per_row):
            cols = st.columns(cols_per_row)
            for j, col in enumerate(cols):
                if i + j < len(filtered_books):
                    book = filtered_books[i + j]
                    with col:
                        st.markdown(f"### {book['image']} {book['title']}")
                        st.write(f"**Author:** {book['author']}")
                        st.write(f"**Category:** {book['category']}")
                        st.write(f"**Price:** ${book['price']:.2f}")
                        st.write(f"**Stock:** {book['stock']} available")
                        with st.expander("Description"):
                            st.write(book['description'])
                        
                        if book['stock'] > 0:
                            if st.button(f"Add to Cart", key=f"add_{book['id']}"):
                                add_to_cart(book)
                                st.success(f"Added '{book['title']}' to cart!")
                                st.rerun()
                        else:
                            st.error("Out of stock")
                        st.divider()

def show_cart():
    """Display shopping cart"""
    st.title("🛒 Shopping Cart")
    
    if not st.session_state.cart:
        st.info("Your cart is empty. Start shopping!")
        return
    
    # Display cart items
    total = 0
    for i, item in enumerate(st.session_state.cart):
        col1, col2, col3, col4 = st.columns([3, 2, 2, 1])
        with col1:
            st.write(f"**{item['title']}**")
            st.caption(f"by {item['author']}")
        with col2:
            st.write(f"${item['price']:.2f}")
        with col3:
            st.write(item['category'])
        with col4:
            if st.button("🗑️", key=f"remove_{i}"):
                remove_from_cart(i)
                st.rerun()
        total += item['price']
        st.divider()
    
    # Cart summary
    st.subheader(f"Total: ${total:.2f}")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Clear Cart", type="secondary"):
            clear_cart()
            st.rerun()
    with col2:
        if st.button("Place Order", type="primary"):
            success, message = place_order()
            if success:
                st.success(message)
                st.balloons()
                st.rerun()
            else:
                st.error(message)

def show_orders():
    """Display user orders"""
    st.title("📦 My Orders")
    
    orders = load_json(ORDERS_FILE, [])
    user_orders = [o for o in orders if o['username'] == st.session_state.username]
    
    if not user_orders:
        st.info("You haven't placed any orders yet.")
        return
    
    for order in reversed(user_orders):
        with st.expander(f"Order #{order['order_id']} - {order['date']} - ${order['total']:.2f}"):
            st.write(f"**Status:** {order['status']}")
            st.write("**Items:**")
            for item in order['items']:
                st.write(f"- {item['title']} by {item['author']} - ${item['price']:.2f}")

def show_admin_panel():
    """Display admin panel"""
    st.title("⚙️ Admin Panel")
    
    tab1, tab2, tab3 = st.tabs(["Manage Books", "View Orders", "Statistics"])
    
    with tab1:
        st.subheader("Manage Books")
        
        # Add new book
        with st.expander("➕ Add New Book"):
            with st.form("add_book_form"):
                title = st.text_input("Title")
                author = st.text_input("Author")
                price = st.number_input("Price", min_value=0.0, step=0.01)
                category = st.text_input("Category")
                description = st.text_area("Description")
                stock = st.number_input("Stock", min_value=0, step=1)
                image = st.text_input("Emoji Icon", value="📖")
                
                if st.form_submit_button("Add Book"):
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
                    st.success("Book added successfully!")
                    st.rerun()
        
        # Edit/Delete existing books
        st.subheader("Existing Books")
        books = get_books()
        for book in books:
            with st.expander(f"{book['image']} {book['title']} by {book['author']}"):
                with st.form(f"edit_book_{book['id']}"):
                    title = st.text_input("Title", value=book['title'])
                    author = st.text_input("Author", value=book['author'])
                    price = st.number_input("Price", value=book['price'], step=0.01)
                    category = st.text_input("Category", value=book['category'])
                    description = st.text_area("Description", value=book['description'])
                    stock = st.number_input("Stock", value=book['stock'], step=1)
                    image = st.text_input("Emoji Icon", value=book['image'])
                    
                    col1, col2 = st.columns(2)
                    with col1:
                        if st.form_submit_button("Update Book"):
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
                            st.success("Book updated!")
                            st.rerun()
                    with col2:
                        if st.form_submit_button("Delete Book", type="secondary"):
                            delete_book(book['id'])
                            st.success("Book deleted!")
                            st.rerun()
    
    with tab2:
        st.subheader("All Orders")
        orders = load_json(ORDERS_FILE, [])
        
        if not orders:
            st.info("No orders yet.")
        else:
            for order in reversed(orders):
                with st.expander(f"Order #{order['order_id']} - {order['username']} - ${order['total']:.2f}"):
                    st.write(f"**Date:** {order['date']}")
                    st.write(f"**Status:** {order['status']}")
                    st.write("**Items:**")
                    for item in order['items']:
                        st.write(f"- {item['title']} - ${item['price']:.2f}")
    
    with tab3:
        st.subheader("Statistics")
        books = get_books()
        orders = load_json(ORDERS_FILE, [])
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Books", len(books))
        with col2:
            st.metric("Total Orders", len(orders))
        with col3:
            total_revenue = sum(order['total'] for order in orders)
            st.metric("Total Revenue", f"${total_revenue:.2f}")
        
        # Books by category
        if books:
            category_counts = {}
            for book in books:
                category_counts[book['category']] = category_counts.get(book['category'], 0) + 1
            
            st.subheader("Books by Category")
            st.bar_chart(category_counts)

# Main app
def main():
    # Initialize data
    initialize_data()
    
    # Show login page if not logged in
    if not st.session_state.logged_in:
        show_login_page()
        return
    
    # Sidebar navigation
    with st.sidebar:
        st.title(f"Welcome, {st.session_state.username}!")
        
        if st.session_state.is_admin:
            st.info("🔑 Admin Account")
            page = st.radio(
                "Navigation",
                ["Browse Books", "Shopping Cart", "My Orders", "Admin Panel"]
            )
        else:
            page = st.radio(
                "Navigation",
                ["Browse Books", "Shopping Cart", "My Orders"]
            )
        
        st.divider()
        
        # Cart summary
        cart_count = len(st.session_state.cart)
        cart_total = sum(item['price'] for item in st.session_state.cart)
        st.write(f"🛒 Cart: {cart_count} items")
        st.write(f"💰 Total: ${cart_total:.2f}")
        
        st.divider()
        
        if st.button("Logout", type="secondary"):
            logout_user()
            st.rerun()
    
    # Display selected page
    if page == "Browse Books":
        show_book_catalog()
    elif page == "Shopping Cart":
        show_cart()
    elif page == "My Orders":
        show_orders()
    elif page == "Admin Panel" and st.session_state.is_admin:
        show_admin_panel()

if __name__ == "__main__":
    main()
