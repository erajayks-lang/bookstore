# 📚 BookStore - Professional Streamlit Edition

A production-grade online bookstore built with Streamlit, featuring advanced user authentication, shopping cart with real-time inventory management, comprehensive order tracking, and powerful admin dashboard.

## ✨ Key Features

### For Customers:
- 🔐 **Secure Authentication** - Professional login/register system with password hashing (SHA-256)
- 📖 **Extensive Book Catalog** - Browse 200+ books across 10 categories with pagination, search, filtering, and sorting
- 🛒 **Smart Shopping Cart** - Real-time calculations with tax, shipping, and quantity management
- 📦 **Order Tracking** - Complete order history with status tracking
- 💳 **Professional Checkout** - Detailed order summary with automatic inventory updates

### For Admins:
- 📊 **Analytics Dashboard** - Real-time metrics, revenue tracking, and category insights
- ➕ **Full CRUD Operations** - Add, edit, and delete books with validation
- 📦 **Order Management** - View all orders, update status, filter and sort
- 👥 **User Management** - View registered users and their purchase history
- ⚠️ **Inventory Alerts** - Automatic low-stock warnings

## 🎨 Professional Design Features

- **Modern UI/UX** - Gradient backgrounds, card layouts, and responsive design
- **Tab-based Navigation** - Intuitive navigation without sidebar clutter
- **Custom Styling** - Professional color schemes and typography
- **Real-time Updates** - Live cart totals and inventory tracking
- **Mobile-Responsive** - Optimized for all screen sizes

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

**Security Note:** In production, change default credentials immediately and implement stronger authentication.

## Production-Grade Features

### Security
- ✅ SHA-256 password hashing
- ✅ Session state management
- ✅ Input validation and sanitization
- ✅ Error handling and logging

### Performance
- ✅ Pagination for large datasets (12 books per page)
- ✅ Efficient JSON-based data storage
- ✅ Optimized rendering with caching

### User Experience
- ✅ Professional gradient UI design
- ✅ Real-time cart calculations (tax + shipping)
- ✅ Automatic inventory updates
- ✅ Advanced search and filtering
- ✅ Multi-level sorting options
- ✅ Responsive card-based layouts

### Admin Tools
- ✅ Comprehensive analytics dashboard
- ✅ Order status management
- ✅ Low stock alerts
- ✅ Category-based insights
- ✅ User activity tracking

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
2. Navigate to "Admin Panel" tab
3. Click "Add New Book" expander
4. Fill in all required fields (marked with *)
5. Click "Add Book"

### Managing Inventory
- Books automatically update stock when orders are placed
- Low stock alerts (< 20 units) appear in Admin Dashboard
- Search and filter books in admin panel for easy management

### Changing Theme
Customize the color scheme by editing `.streamlit/config.toml`:
```toml
[theme]
primaryColor = "#FF6B6B"  # Your brand color
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#262730"
font = "sans serif"
```

### Adjusting Tax and Shipping
In `bookstore_app.py`, modify the `place_order()` function:
```python
tax = subtotal * 0.08  # Change to your tax rate
shipping = 5.99 if subtotal < 50 else 0  # Adjust free shipping threshold
```

## Advanced Features

### Pagination
- 12 books per page in catalog
- Easy navigation with First/Previous/Next/Last buttons
- Automatic page reset when filters change

### Smart Cart
- Quantity tracking per item
- Real-time subtotal, tax, and shipping calculations
- Free shipping on orders over $50
- Cart persists during session

### Order Management
- Automatic status tracking (Pending → Processing → Shipped → Delivered)
- Order history with detailed breakdowns
- Admin can update order status

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

### Database Integration
- [ ] PostgreSQL for persistent storage (Supabase recommended)
- [ ] MongoDB for scalable document storage
- [ ] Redis for session caching

### Advanced Features
- [ ] Payment gateway (Stripe/PayPal)
- [ ] Email notifications (order confirmations, shipping updates)
- [ ] Book ratings and reviews
- [ ] Image uploads for book covers (S3 integration)
- [ ] Wishlist functionality
- [ ] Discount codes and promotions
- [ ] Advanced search with AI recommendations
- [ ] Export orders to CSV/PDF
- [ ] Multi-currency support
- [ ] Real-time stock notifications

### Enhanced Security
- [ ] OAuth integration (Google, GitHub)
- [ ] Two-factor authentication (2FA)
- [ ] Rate limiting for API calls
- [ ] CAPTCHA for registration
- [ ] Enhanced password requirements
- [ ] Session timeout management

### Analytics & Reporting
- [ ] Sales dashboards with charts
- [ ] Customer behavior analytics
- [ ] Inventory forecasting
- [ ] Revenue projections
- [ ] Export analytics reports

## Performance Optimization

The current implementation is optimized for:
- **Small to medium datasets** (< 1000 books, < 5000 orders)
- **Single-user admin** workflows
- **Session-based** data storage

For larger scale deployments:
1. Implement database backend (PostgreSQL/MongoDB)
2. Add server-side caching (Redis)
3. Implement pagination for all data views
4. Use async operations for large queries
5. Add CDN for static assets

## Support

For issues or questions:
1. Check the Streamlit documentation: https://docs.streamlit.io
2. Review the code comments in `bookstore_app.py`
3. Create an issue on GitHub

## License

MIT License - Feel free to modify and use for your projects!

---

**Built with ❤️ using Streamlit**
