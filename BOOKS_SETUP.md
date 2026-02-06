# 📚 Setting Up 200 Books

## Quick Setup

The BookStore app comes with 200 pre-configured books across 10 categories. Here's how to set them up:

### Method 1: Automatic Setup (Recommended)

1. **Place `books_200.json` in the same directory as `bookstore_app.py`**
   ```
   your-project/
   ├── bookstore_app.py
   ├── books_200.json          ← Place here
   ├── requirements.txt
   └── .streamlit/
       └── config.toml
   ```

2. **Run the app**
   ```bash
   streamlit run bookstore_app.py
   ```

3. **The app will automatically:**
   - Detect `books_200.json`
   - Load all 200 books
   - Create `books.json` for persistent storage
   - You're ready to go!

### Method 2: Manual Generation

If you don't have `books_200.json`:

1. **Run the generator script**
   ```bash
   python3 generate_books.py
   ```

2. **This creates `books_200.json` with 200 books**

3. **Start the app**
   ```bash
   streamlit run bookstore_app.py
   ```

### Method 3: Fallback (Minimal Books)

If neither file exists, the app will create 3 sample books automatically. You can then:
- Add more books through the Admin Panel
- Or follow Method 1 or 2 above

## Book Distribution

The 200 books are distributed across these categories:

| Category | Count | Price Range |
|----------|-------|-------------|
| Fiction | 40 | $11.99 - $18.99 |
| Science Fiction | 30 | $11.99 - $18.99 |
| Fantasy | 30 | $14.99 - $20.99 |
| Mystery | 25 | $12.99 - $16.99 |
| Romance | 20 | $11.99 - $17.99 |
| Non-Fiction | 20 | $15.99 - $19.99 |
| Biography | 15 | $12.99 - $19.99 |
| History | 10 | $16.99 - $19.99 |
| Self-Help | 5 | $14.99 - $16.99 |
| Children | 5 | $8.99 - $12.99 |
| **Total** | **200** | **$8.99 - $20.99** |

## Verifying Setup

After starting the app:

1. **Login as admin** (username: `admin`, password: `admin123`)
2. **Go to Admin Panel** → **Analytics** tab
3. **Check "Total Books" metric** - should show 200

## Customizing Books

### Adding More Books

1. Login as admin
2. Go to **Admin Panel** → **Manage Books**
3. Click **Add New Book**
4. Fill in the details
5. Click **Add Book**

### Editing Existing Books

1. Admin Panel → **Manage Books**
2. Use search/filter to find the book
3. Expand the book card
4. Edit details
5. Click **Update**

### Bulk Import

To add many books at once:

1. Edit `books_200.json` directly
2. Add your books following the format:
   ```json
   {
     "id": 201,
     "title": "Your Book Title",
     "author": "Author Name",
     "price": 15.99,
     "category": "Fiction",
     "description": "Book description",
     "stock": 50,
     "image": "📕"
   }
   ```
3. Delete `books.json` (it will regenerate)
4. Restart the app

## Troubleshooting

### "No books showing up"
- Check that `books_200.json` is in the correct directory
- Look for `books.json` - if it exists but is empty, delete it
- Restart the app

### "Only 3 books available"
- `books_200.json` wasn't found
- Run `python3 generate_books.py` to create it
- Restart the app

### "Books reset after restart" (Streamlit Cloud)
- This is normal - Streamlit Cloud has ephemeral storage
- Books reset when the app restarts
- Solution: Integrate a persistent database (see PRODUCTION_CHECKLIST.md)

## File Structure

```
your-bookstore/
├── bookstore_app.py          # Main application
├── books_200.json            # 200 pre-configured books (source)
├── generate_books.py         # Script to generate books_200.json
├── requirements.txt          # Python dependencies
├── .streamlit/
│   └── config.toml          # Streamlit configuration
├── README.md                 # Full documentation
├── DEPLOYMENT_GUIDE.md       # Deployment instructions
└── PRODUCTION_CHECKLIST.md   # Production readiness guide

# Generated at runtime:
├── books.json               # Active book database
├── users.json               # User accounts
└── orders.json              # Order history
```

## Categories Explained

- **Fiction** (40): Literary fiction, contemporary novels
- **Science Fiction** (30): Sci-fi, dystopian, space opera
- **Fantasy** (30): Epic fantasy, urban fantasy, magical realism
- **Mystery** (25): Detective, thriller, psychological suspense
- **Romance** (20): Contemporary, historical, romantic comedy
- **Non-Fiction** (20): Science, history, psychology, business
- **Biography** (15): Memoirs, autobiographies
- **History** (10): World history, American history
- **Self-Help** (5): Personal development, productivity
- **Children** (5): Picture books, middle grade

## Pro Tips

1. **Pagination**: With 200 books, pagination (12 per page) keeps the UI clean
2. **Search & Filter**: Essential for finding books quickly
3. **Category Balance**: Well-distributed across popular categories
4. **Price Range**: $8.99-$20.99 covers most book price points
5. **Stock Levels**: Varied (35-80) for realistic inventory management

---

**Need Help?** Check the main [README.md](README.md) or [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)
