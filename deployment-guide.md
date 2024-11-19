# Deploying to Streamlit Cloud

## 1. Prepare Your GitHub Repository
1. Create a new repository on GitHub
2. Push your code to the repository:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/your-username/your-repo-name.git
   git push -u origin main
   ```

## 2. Deploy on Streamlit Cloud
1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with your GitHub account
3. Click "New app"
4. Select your repository, branch, and Python file:
   - Repository: Choose your GitHub repository
   - Branch: main
   - Main file path: app.py
5. Click "Deploy!"

## 3. Important Settings
- Ensure all your dependencies are listed in `requirements.txt`
- If you have secrets/API keys:
  1. Go to your app settings
  2. Find "Secrets" section
  3. Add your secrets there

## 4. Monitoring
- Your app will be assigned a URL like: `https://your-app-name.streamlit.app`
- You can monitor app health and logs in the Streamlit Cloud dashboard
- The app will automatically redeploy when you push changes to GitHub

## 5. Resources
- Free tier includes:
  - 1 GB RAM
  - Public repositories only
  - Unlimited apps
  - Basic app analytics
