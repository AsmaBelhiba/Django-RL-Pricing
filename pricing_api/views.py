from django.http import HttpResponse
from django.templatetags.static import static

def root_view(request):
    favicon_url = static("images/meilleur-prix.png")  

    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Pricing API | Status</title>
        <link rel="icon" type="image/png" href="{favicon_url}" />
        <style>
            :root {{
                --bg-color: #f9fafb;
                --text-color: #111827;
                --accent-color: #2563eb;
                --card-bg: #ffffff;
                --border-radius: 12px;
            }}
            body {{
                font-family: 'Inter', system-ui, sans-serif;
                background-color: var(--bg-color);
                color: var(--text-color);
                margin: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                padding: 1rem;
            }}
            .container {{
                max-width: 720px;
                background: var(--card-bg);
                padding: 2rem 2.5rem;
                border-radius: var(--border-radius);
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.06);
                text-align: center;
            }}
            h1 {{
                font-size: 1.8rem;
                margin-bottom: 1rem;
                color: var(--accent-color);
            }}
            p.description {{
                font-size: 1rem;
                line-height: 1.6;
                color: #374151;
                margin-bottom: 2rem;
            }}
            .tech-stack {{
                display: flex;
                justify-content: center;
                flex-wrap: wrap;
                gap: 0.75rem;
                margin-bottom: 2rem;
            }}
            .badge {{
                background-color: #e0e7ff;
                color: #1e40af;
                padding: 0.4rem 0.75rem;
                border-radius: 999px;
                font-size: 0.85rem;
                font-weight: 600;
            }}
            .endpoints {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
                gap: 1rem;
            }}
            .endpoint-card {{
                background-color: #f3f4f6;
                padding: 1rem;
                border-radius: var(--border-radius);
                text-decoration: none;
                color: #1f2937;
                font-weight: 500;
                transition: all 0.2s ease;
                box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
            }}
            .endpoint-card:hover {{
                background-color: #e5e7eb;
                transform: translateY(-2px);
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 Pricing API is Live</h1>
            <p class="description">
                A backend service for dynamic product pricing using <strong>Django</strong>, <strong>DRF</strong>, 
                <strong>Celery</strong>, and <strong>Reinforcement Learning</strong>. This API powers 
                real-time pricing decisions based on trained machine learning models and scheduled updates.
            </p>
            <div class="tech-stack">
                <div class="badge">Django</div>
                <div class="badge">DRF</div>
                <div class="badge">Celery</div>
                <div class="badge">GraphQL</div>
                <div class="badge">RL Agent</div>
            </div>
            <div class="endpoints">
                <a href="/admin/" class="endpoint-card">/admin</a>
                <a href="/graphql/" class="endpoint-card">/graphql</a>
                <a href="/rest/" class="endpoint-card">/rest</a>
            </div>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html_content)
