# 📚 BookStore - Streamlit Edition

A complete online bookstore built with Streamlit, featuring user authentication, shopping cart, order management, and admin panel.

## Features

### For Customers:
- 🔐 User registration and login
- 📖 Browse books with search and filtering
- 🛒 Shopping cart functionality
- 📦 Order history tracking
- 💳 Simple checkout process

### For Admins:
- ➕ Add, edit, and delete books
- 📊 View all orders
- 📈 View sales statistics
- 📚 Manage inventory

## Quick Start (Local Testing)

1. **Install Python** (3.8 or higher)

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app:**
   ```bash
   streamlit run bookstore_app.py
   ```

4. **Open your browser** to `http://localhost:8501`

5. **Login with demo account:**
   - Username: `admin`
   - Password: `admin123`

## Deploy to Streamlit Cloud (FREE)

### Step 1: Prepare Your GitHub Repository

1. **Create a new repository on GitHub:**
   - Go to https://github.com/new
   - Name it `bookstore-streamlit`
   - Make it public
   - Don't initialize with README

2. **Push your code to GitHub:**
   ```bash
   # In your project folder
   git init
   git add .
   git commit -m "Initial commit - BookStore app"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/bookstore-streamlit.git
   git push -u origin main
   ```

### Step 2: Deploy on Streamlit Cloud

1. **Go to** https://share.streamlit.io/

2. **Sign in** with your GitHub account

3. **Click "New app"**

4. **Fill in the deployment settings:**
   - Repository: `YOUR_USERNAME/bookstore-streamlit`
   - Branch: `main`
   - Main file path: `bookstore_app.py`

5. **Click "Deploy"**

6. **Wait 2-3 minutes** for deployment to complete

7. **Your app will be live** at `https://YOUR_USERNAME-bookstore-streamlit.streamlit.app`

## Default Credentials

**Admin Account:**
- Username: `admin`
- Password: `admin123`

**You can create new user accounts** through the registration page.

## Data Storage

The app uses JSON files for data storage:
- `users.json` - User accounts
- `books.json` - Book catalog
- `orders.json` - Order history

**Note:** Streamlit Cloud has ephemeral storage, meaning data will reset when the app restarts. For production use, consider integrating a database like:
- Supabase
- MongoDB Atlas
- Google Sheets (via gspread)

## Customization

### Adding Books
1. Login as admin
2. Go to "Admin Panel"
3. Click "Add New Book"
4. Fill in book details

### Changing Theme
Add a `.streamlit/config.toml` file:
```toml
[theme]
primaryColor = "#FF4B4B"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#262730"
font = "sans serif"
```

## Project Structure

```
bookstore-streamlit/
│
├── bookstore_app.py      # Main application
├── requirements.txt      # Python dependencies
├── README.md            # This file
│
└── Data files (auto-generated):
    ├── users.json
    ├── books.json
    └── orders.json
```

## Troubleshooting

**App won't start:**
- Check that `streamlit` is installed: `pip install streamlit`
- Ensure Python version is 3.8+

**Data disappears after restart:**
- This is normal on Streamlit Cloud (ephemeral storage)
- Implement persistent database for production

**Login issues:**
- Use default admin credentials: `admin` / `admin123`
- Register a new account if needed

## Future Enhancements

- [ ] Integrate persistent database (PostgreSQL, MongoDB)
- [ ] Add payment gateway integration
- [ ] Implement email notifications
- [ ] Add book ratings and reviews
- [ ] Image uploads for book covers
- [ ] Advanced search with filters
- [ ] Wishlist functionality
- [ ] Discount codes and promotions

## Support

For issues or questions:
1. Check the Streamlit documentation: https://docs.streamlit.io
2. Review the code comments in `bookstore_app.py`
3. Create an issue on GitHub

## License

MIT License - Feel free to modify and use for your projects!

---

**Built with ❤️ using Streamlit**
