# 🚀 Deployment Guide for Smart Waste Sort App

## 📋 Overview
This guide will help you deploy your mobile app so it works without your local computer running the backend.

## 🎯 Quick Solutions

### Option 1: Deploy Backend to Cloud (Recommended)

#### **Step 1: Prepare Backend for Deployment**

1. **Create `requirements.txt`** (if not exists):
```bash
cd backend
pip freeze > requirements.txt
```

2. **Create `Procfile`** (for Heroku):
```bash
# backend/Procfile
web: python main.py
```

3. **Update `main.py`** for production:
```python
# Add at the top of main.py
import os

# Update the run line at the bottom
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
```

#### **Step 2: Deploy to Heroku**

1. **Install Heroku CLI** and login:
```bash
# Download from: https://devcenter.heroku.com/articles/heroku-cli
heroku login
```

2. **Create Heroku app**:
```bash
cd backend
heroku create your-app-name
```

3. **Deploy**:
```bash
git add .
git commit -m "Deploy backend"
git push heroku main
```

4. **Get your deployed URL**:
```bash
heroku info
# Look for "Web URL" - it will be like: https://your-app-name.herokuapp.com
```

#### **Step 3: Update Mobile App Configuration**

1. **Update `SmartWasteSortApp/src/config/api.js`**:
```javascript
// Change this line:
const CURRENT_ENV = ENV.PRODUCTION;

// And update the production URL:
const API_URLS = {
  [ENV.DEVELOPMENT]: 'http://192.168.0.101:5000',
  [ENV.PRODUCTION]: 'https://your-app-name.herokuapp.com', // Your Heroku URL
  [ENV.STAGING]: 'https://your-staging-backend.herokuapp.com',
};
```

2. **Rebuild your APK**:
```bash
cd SmartWasteSortApp
npx react-native run-android --variant=release
```

### Option 2: Use Firebase (Alternative Backend)

#### **Step 1: Set up Firebase**

1. **Go to [Firebase Console](https://console.firebase.google.com/)**
2. **Create a new project**
3. **Enable Firestore Database**
4. **Enable Storage** (for images)
5. **Get your config**:
   - Go to Project Settings
   - Copy the config object

#### **Step 2: Update Mobile App for Firebase**

1. **Install Firebase**:
```bash
cd SmartWasteSortApp
npm install firebase
```

2. **Update `SmartWasteSortApp/src/config/api.js`**:
```javascript
// Set to use Firebase
const CURRENT_ENV = ENV.PRODUCTION;

// Update Firebase config with your actual values
const FIREBASE_CONFIG = {
  apiKey: "your-actual-api-key",
  authDomain: "your-project.firebaseapp.com",
  projectId: "your-project-id",
  storageBucket: "your-project.appspot.com",
  messagingSenderId: "your-sender-id",
  appId: "your-app-id"
};
```

3. **Create Firebase service** (`SmartWasteSortApp/src/services/firebase.js`):
```javascript
import { initializeApp } from 'firebase/app';
import { getFirestore, collection, addDoc, getDocs, updateDoc, doc } from 'firebase/firestore';
import { getStorage, ref, uploadBytes, getDownloadURL } from 'firebase/storage';
import { FIREBASE_CONFIG } from '../config/api';

// Initialize Firebase
const app = initializeApp(FIREBASE_CONFIG);
const db = getFirestore(app);
const storage = getStorage(app);

// Firebase API functions
export const firebaseAPI = {
  // Submit report
  submitReport: async (reportData, imageUri) => {
    try {
      // Upload image first
      const imageRef = ref(storage, `reports/${Date.now()}.jpg`);
      const response = await fetch(imageUri);
      const blob = await response.blob();
      await uploadBytes(imageRef, blob);
      const imageUrl = await getDownloadURL(imageRef);

      // Save report data
      const docRef = await addDoc(collection(db, 'reports'), {
        ...reportData,
        imageUrl,
        createdAt: new Date(),
        status: 'pending'
      });

      return { success: true, id: docRef.id };
    } catch (error) {
      console.error('Error submitting report:', error);
      return { success: false, error: error.message };
    }
  },

  // Get dashboard data
  getDashboard: async () => {
    try {
      const querySnapshot = await getDocs(collection(db, 'reports'));
      const reports = [];
      querySnapshot.forEach((doc) => {
        reports.push({ id: doc.id, ...doc.data() });
      });
      return { success: true, recent_reports: reports };
    } catch (error) {
      console.error('Error getting dashboard:', error);
      return { success: false, error: error.message };
    }
  },

  // Update status
  updateStatus: async (reportId, status) => {
    try {
      const reportRef = doc(db, 'reports', reportId);
      await updateDoc(reportRef, { status });
      return { success: true, message: 'Status updated successfully' };
    } catch (error) {
      console.error('Error updating status:', error);
      return { success: false, error: error.message };
    }
  }
};
```

## 🔧 Environment Switching

### **Development Mode** (Local backend):
```javascript
// In SmartWasteSortApp/src/config/api.js
const CURRENT_ENV = ENV.DEVELOPMENT;
```

### **Production Mode** (Deployed backend):
```javascript
// In SmartWasteSortApp/src/config/api.js
const CURRENT_ENV = ENV.PRODUCTION;
```

## 📱 Building Production APK

### **Step 1: Generate Keystore** (if not done):
```bash
cd SmartWasteSortApp/android
keytool -genkey -v -keystore my-release-key.keystore -alias my-key-alias -keyalg RSA -keysize 2048 -validity 10000
```

### **Step 2: Configure Signing**:
Edit `android/app/build.gradle`:
```gradle
android {
    ...
    signingConfigs {
        release {
            storeFile file('my-release-key.keystore')
            storePassword 'your-store-password'
            keyAlias 'my-key-alias'
            keyPassword 'your-key-password'
        }
    }
    buildTypes {
        release {
            signingConfig signingConfigs.release
            minifyEnabled true
            proguardFiles getDefaultProguardFile('proguard-android.txt'), 'proguard-rules.pro'
        }
    }
}
```

### **Step 3: Build APK**:
```bash
cd SmartWasteSortApp
npx react-native run-android --variant=release
```

The APK will be in: `android/app/build/outputs/apk/release/app-release.apk`

## 🌐 Alternative Deployment Options

### **Railway** (Alternative to Heroku):
1. Go to [railway.app](https://railway.app)
2. Connect your GitHub repo
3. Deploy automatically

### **Render** (Alternative to Heroku):
1. Go to [render.com](https://render.com)
2. Create new Web Service
3. Connect your repo and deploy

### **Vercel** (For static frontend):
1. Go to [vercel.com](https://vercel.com)
2. Import your project
3. Deploy automatically

## 🔍 Testing Your Deployment

### **Test Backend**:
```bash
# Test your deployed backend
curl https://your-app-name.herokuapp.com/api/health
```

### **Test Mobile App**:
1. Install the new APK
2. Check if it connects to the deployed backend
3. Test all features (submit report, view dashboard, etc.)

## 🚨 Common Issues & Solutions

### **Issue 1: CORS Errors**
**Solution**: Add CORS headers to your Flask backend:
```python
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
```

### **Issue 2: Image Upload Fails**
**Solution**: Use Firebase Storage or configure your cloud storage properly.

### **Issue 3: Database Connection**
**Solution**: Use cloud database (MongoDB Atlas, PostgreSQL on Heroku, etc.)

### **Issue 4: Environment Variables**
**Solution**: Set environment variables in your cloud platform dashboard.

## 📞 Support

If you encounter issues:
1. Check the console logs in your mobile app
2. Check the backend logs in your cloud platform
3. Test the API endpoints directly with curl or Postman

## 🎉 Success Checklist

- [ ] Backend deployed to cloud
- [ ] Mobile app configured for production
- [ ] APK built with production settings
- [ ] All features tested on deployed backend
- [ ] Images upload and display correctly
- [ ] Dashboard loads reports from cloud
- [ ] Status updates work properly

**Your app is now ready to work without your local computer!** 🚀 