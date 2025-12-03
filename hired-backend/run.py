from app import create_app

app = create_app()

@app.route('/')
def home_page():
    return 'Backend is running successfully! 🚀  Check the following links: /api/v1/auth/health , /api/v1/jobs/health , /api/v1/user-jobs/health'

if __name__ == "__main__":
    app.run(debug=True)
