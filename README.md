# AI Powered Blog Post Generator

An intelligent blog post generation system that uses AI to create SEO-optimized content. This application automatically generates blog posts based on keywords, incorporates SEO best practices, and provides a clean web interface for content management.

## 🚀 Live Demo

### Quick Start
1. **Start the application:**
   ```bash
   python app.py
   ```

2. **Access the web interface:**
   - Open your browser and navigate to `http://localhost:5000`
   - View all generated blog posts on the main page

3. **Generate a new blog post:**
   - Visit: `http://localhost:5000/generate?keyword=artificial-intelligence`
   - Or try: `http://localhost:5000/generate?keyword=machine-learning`

4. **View generated content:**
   - Click on any post from the main page
   - Or access directly: `http://localhost:5000/post/artificial-intelligence`

### Demo Features
- **AI Content Generation**: Enter any keyword and watch AI create a comprehensive blog post
- **SEO Integration**: View real-time SEO metrics including search volume, keyword difficulty, and CPC
- **Responsive Design**: Clean, modern interface that works on all devices
- **Content Management**: View, organize, and delete generated posts
- **Automated Scheduling**: Daily post generation with random keywords

### Sample Output
The system generates structured blog posts with:
- Compelling titles optimized for SEO
- Engaging introductions with hooks
- Comprehensive main content with examples
- Future outlook and trends
- Actionable conclusions
- Verified sources and references
- Real-time SEO performance metrics

## Features

- 🤖 AI-powered blog post generation using Mistral AI's Medium model
- 📊 SEO optimization with real-time metrics and dedicated template
- 📝 Markdown to HTML conversion with code highlighting
- 🔄 Automated daily post generation with random keywords
- 📱 Responsive web interface
- 🔍 Source management and verification
- 📈 SEO performance tracking with detailed metrics
- 🗑️ Content management system
- 🔐 Secure API key management
- 📦 JSON-based content storage

## Prerequisites

- Python 3.8 or higher
- Mistral AI API key
- Flask 2.3.3
- Virtual environment (recommended)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/HarshaVardhanMannem/AI-powered-Blog-post-Generator.git
cd AI-powered-Blog-post-Generator
```

2. Create and activate a virtual environment:
```bash
# Windows
python -m venv blogEnv
.\blogEnv\Scripts\activate

# Linux/Mac
python3 -m venv blogEnv
source blogEnv/bin/activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory and add your API keys:
```env
MISTRAL_API_KEY=your_mistral_api_key_here
```

## Project Structure

```
AI-powered-Blog-post-Generator/
├── app.py                 # Main Flask application
├── ai_generator.py        # AI content generation logic
├── seo_fetcher.py         # SEO data fetching
├── seo_template.html      # SEO metrics template
├── requirements.txt       # Project dependencies
├── data/                  # Data storage
│   └── blogsDb.json      # Blog posts database
├── generated_posts/       # Generated content storage
├── templates/            # HTML templates
│   ├── index.html        # Main page template
│   └── blog_post.html    # Blog post template
├── static/              # Static assets
│   ├── css/            # Stylesheets
│   └── js/             # JavaScript files
└── blogEnv/            # Virtual environment
```

## Usage

1. Start the Flask application:
```bash
python app.py
```

2. Access the web interface:
- Open your browser and navigate to `http://localhost:5000`
- The main page will display all generated blog posts
- Click on any post to view its full content

3. Generate a new blog post:
- Use the `/generate` endpoint with a keyword parameter
- Example: `http://localhost:5000/generate?keyword=wireless-earbuds`

4. View a specific post:
- Access posts using the `/post/<filename>` endpoint
- Example: `http://localhost:5000/post/wireless-earbuds`

## API Endpoints

### Main Endpoints

- `GET /`: Home page with list of all blog posts
- `GET /post/<filename>`: View a specific blog post
- `GET /generate`: Generate a new blog post
  - Query Parameters:
    - `keyword`: The topic for the blog post
  - Returns: JSON with generated content and SEO data
- `POST /delete_post/<keyword>`: Delete a blog post
  - Returns: Success/error message
- `GET /health`: Health check endpoint
  - Returns: Application status

### Helper Functions

- `load_blog_posts()`: Load posts from JSON database
- `save_blog_posts()`: Save posts to JSON database
- `sanitize_word()`: Sanitize keywords for filenames
- `extract_title_from_markdown()`: Extract titles from content
- `save_post_json()`: Save generated posts as JSON
- `generate_daily_post()`: Scheduled post generation

## Error Handling

The application includes comprehensive error handling for:

### API and Network Errors
- API key validation and authentication
- Network connectivity issues
- Rate limiting and timeout handling
- Invalid API responses

### Content Generation
- Invalid keyword handling
- Content validation
- Markdown parsing errors
- SEO data fetching failures

### File Operations
- File read/write permissions
- Directory creation
- JSON parsing and validation
- Database operations

### Template Rendering
- Missing template files
- Template syntax errors
- Variable substitution errors

### User Input
- Input validation
- Sanitization
- Malformed requests
- Invalid parameters

## Automated Features

### Content Generation
- Daily post generation using random keywords
- Keyword selection from predefined list
- Automatic SEO data fetching
- Content validation and formatting

### SEO Integration
- Real-time SEO metrics fetching
- Keyword difficulty analysis
- Search volume tracking
- CPC (Cost Per Click) monitoring
- Custom SEO template integration

### Content Management
- Automatic file organization
- JSON-based content storage
- Markdown to HTML conversion
- Source verification and management

### System Maintenance
- Health check monitoring
- Error logging and tracking
- Database backup and recovery
- Cache management

## Content Generation

The system generates blog posts with the following structure:

1. Title
   - Accurate and compelling
   - Contains attention-grabbing words
   - Appeals to beginners and general audiences
   - Naturally incorporates the main keyword

2. Introduction (2 paragraphs)
   - Engaging hook or question
   - Clear topic explanation
   - Relevance to readers
   - Value proposition

3. Main Content
   - Simple explanations with analogies
   - Practical examples
   - Detailed explanations
   - Step-by-step breakdowns
   - Common misconceptions
   - Benefits and challenges
   - Current trends

4. Future Outlook
   - Emerging trends
   - Potential challenges
   - Opportunities
   - What to watch for

5. Conclusion
   - Key takeaways
   - Actionable next steps
   - Call-to-action

6. Sources (3-5 verified sources)
   - Reputable sources
   - Verified links
   - Brief descriptions

## SEO Integration

Each generated post includes:
- Search volume with monthly statistics
- Keyword difficulty score (0-100)
- Average CPC (Cost Per Click) in USD
- SEO-optimized content structure
- Custom SEO template integration
- Performance metrics tracking

## Automated Features

- Daily post generation using random keywords
- SEO data fetching and integration
- Markdown to HTML conversion
- Source verification and management

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Mistral AI Models
- Flask Framework
- Python Community

## Support

For support, please open an issue in the GitHub repository or contact the maintainers.

## Future Enhancements

- [ ] Social media integration
- [ ] Analytics dashboard
- [ ] Multi-language support
- [ ] Custom AI model integration
- [ ] Advanced SEO optimization
- [ ] Content scheduling system
- [ ] User authentication system
- [ ] Content versioning
- [ ] Automated image generation
- [ ] API rate limiting and monitoring 