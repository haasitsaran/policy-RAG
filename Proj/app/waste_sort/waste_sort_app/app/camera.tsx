import React, { useRef, useState, useEffect } from 'react';
import { View, Text, StyleSheet, TouchableOpacity, Platform } from 'react-native';
import { Camera } from 'expo-camera';
import { Ionicons } from '@expo/vector-icons';

export default function CameraScreen() {
  if (Platform.OS === 'web') {
    return (
      <View style={styles.container}>
        <Text style={styles.text}>
          Camera is not supported in the web version. Please use a real device.
        </Text>
      </View>
    );
  }

  const [hasPermission, setHasPermission] = useState(null);
  const cameraRef = useRef(null);

  useEffect(() => {
    (async () => {
      const { status } = await Camera.requestCameraPermissionsAsync();
      setHasPermission(status === 'granted');
    })();
  }, []);

  if (hasPermission === null) {
    return <View style={styles.container}><Text style={styles.text}>Requesting camera permission...</Text></View>;
  }
  if (hasPermission === false) {
    return <View style={styles.container}><Text style={styles.text}>No access to camera</Text></View>;
  }

  return (
    <View style={styles.container}>
      <Camera
        style={{ flex: 1, width: '100%' }}
        ref={cameraRef}
        type={Camera.Constants.Type.back}
      />
      <TouchableOpacity
        style={styles.captureButton}
        onPress={async () => {
          if (cameraRef.current) {
            const photo = await cameraRef.current.takePictureAsync();
            // handle photo
          }
        }}
      >
        <Ionicons name="camera" size={36} color="#fff" />
      </TouchableOpacity>
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#181A20', justifyContent: 'center', alignItems: 'center' },
  captureButton: { position: 'absolute', bottom: 40, alignSelf: 'center', backgroundColor: '#23252C', borderRadius: 40, padding: 18, borderWidth: 3, borderColor: '#fff' },
  text: { color: '#fff', fontSize: 20, textAlign: 'center' },
}); 