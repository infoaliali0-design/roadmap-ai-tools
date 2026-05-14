# Deployment Guide - Roadmap AI Tools

## Production Checklist

- [ ] All environment variables configured
- [ ] Database backups enabled
- [ ] SSL certificates installed
- [ ] CDN configured
- [ ] Email service configured
- [ ] Security headers configured
- [ ] Rate limiting enabled
- [ ] Logging configured
- [ ] Error monitoring setup
- [ ] Analytics configured

## Frontend Deployment (Vercel)

### Option 1: Deploy via Vercel CLI

```bash
# Install Vercel CLI
npm i -g vercel

# Login to Vercel
vercel login

# Deploy from frontend directory
cd frontend
vercel
```

Follow the prompts:
- Scope: Personal
- Project name: roadmap-ai-tools
- Build command: `npm run build`
- Output directory: `.next`

### Option 2: Deploy via GitHub Integration

1. Push code to GitHub
2. Go to [Vercel Dashboard](https://vercel.com)
3. Click "Add New" → "Project"
4. Import your GitHub repository
5. Configure project:
   - Framework: Next.js
   - Root directory: `frontend`
   - Build command: `npm run build`
   - Output: `.next`
6. Add environment variables:
   ```env
   NEXT_PUBLIC_API_URL=https://api.roadmapaitools.com
   NEXT_PUBLIC_GOOGLE_CLIENT_ID=your-production-id
   NEXT_PUBLIC_APP_URL=https://roadmapaitools.com
   ```
7. Click Deploy

## Backend Deployment (Railway)

### Option 1: Deploy via Railway CLI

```bash
# Install Railway CLI
npm i -g @railway/cli

# Login to Railway
railway login

# Initialize project
cd backend
railway init

# Deploy
railway up
```

### Option 2: Deploy via GitHub Integration

1. Go to [Railway Dashboard](https://railway.app)
2. Click "New Project"
3. Select "Deploy from GitHub repo"
4. Connect GitHub and select repository
5. Select Python environment
6. Configure environment variables:
   ```env
   FLASK_ENV=production
   FLASK_APP=run.py
   DATABASE_URL=your-mongodb-url
   JWT_SECRET_KEY=your-production-secret
   GOOGLE_CLIENT_ID=your-production-id
   GOOGLE_CLIENT_SECRET=your-production-secret
   CORS_ORIGINS=https://roadmapaitools.com
   ```
7. Deploy

## Database Deployment (MongoDB Atlas)

### Production Setup

1. Go to [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
2. Create production cluster:
   - Cluster name: "roadmap-ai-production"
   - Cloud provider: AWS (or your preference)
   - Region: Closest to your users
3. Enable security features:
   - Encryption at rest
   - Automated backups (daily)
4. Create dedicated user:
   - Username: `roadmap_prod_user`
   - Generate strong password
5. Whitelist IPs:
   - Add Vercel IP
   - Add Railway IP

## Domain Configuration

### Point Domain to Vercel (Frontend)

1. Go to domain registrar
2. Update DNS records:

```
Type: A
Name: @
Value: 76.76.19.20

Type: CNAME
Name: www
Value: cname.vercel-dns.com
```

### Point API Subdomain to Railway (Backend)

1. Go to domain registrar
2. Add DNS record:

```
Type: CNAME
Name: api
Value: your-railway-domain.railway.app
```

## SSL/TLS Certificates

**Vercel:** Automatic SSL certificates (free)  
**Railway:** Automatic SSL certificates (free)

## Force HTTPS

**Next.js (next.config.js):**
```javascript
const nextConfig = {
  async redirects() {
    return [
      {
        source: '/:path*',
        destination: 'https://roadmapaitools.com/:path*',
        permanent: true,
      },
    ];
  },
};

module.exports = nextConfig;
```

## Monitoring & Logging

### Vercel Analytics
- Available in Vercel dashboard
- Real-time performance metrics

### Railway Logs
```bash
railway logs
```

## Rollback Procedure

### Vercel Rollback
1. Go to Deployments
2. Select previous version
3. Click "Promote to Production"

### Railway Rollback
```bash
railway rollback
```

## Performance Optimization

### Image Optimization
- Use Next.js Image component
- Enable automatic WebP conversion

### Database Indexing
```javascript
db.tools.createIndex({ slug: 1 });
db.blog_posts.createIndex({ published_date: -1 });
db.users.createIndex({ email: 1 }, { unique: true });
```

## Support

For deployment issues:
- Check Vercel/Railway logs
- Contact platform support
- Email: support@roadmapaitools.com
