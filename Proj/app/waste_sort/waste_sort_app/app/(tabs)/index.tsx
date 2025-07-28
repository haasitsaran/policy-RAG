import React, { useEffect, useRef } from 'react';
import {
  View,
  Text,
  StyleSheet,
  Dimensions,
  TouchableOpacity,
  Animated,
} from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import { router } from 'expo-router';

const { width, height } = Dimensions.get('window');

const quotes = [
  "Every piece of waste is a resource in disguise",
  "Small actions, big impact on our planet",
  "Sort today, save tomorrow",
  "Your choices shape our future",
  "Together we can make a difference"
];

const colors = [
  ['#667eea', '#764ba2'],
  ['#f093fb', '#f5576c'],
  ['#4facfe', '#00f2fe'],
  ['#43e97b', '#38f9d7'],
  ['#fa709a', '#fee140'],
];

export default function OnboardingScreen() {
  const fadeAnim = useRef(new Animated.Value(0)).current;
  const slideAnim = useRef(new Animated.Value(50)).current;
  const gradientAnim = useRef(new Animated.Value(0)).current;

  useEffect(() => {
    // Animate quote on mount
    Animated.parallel([
      Animated.timing(fadeAnim, {
        toValue: 1,
        duration: 1000,
        useNativeDriver: true,
      }),
      Animated.timing(slideAnim, {
        toValue: 0,
        duration: 1000,
        useNativeDriver: true,
      }),
    ]).start();

    // Animate gradient colors
    const animateGradient = () => {
      Animated.timing(gradientAnim, {
        toValue: 1,
        duration: 3000,
        useNativeDriver: false,
      }).start(() => {
        gradientAnim.setValue(0);
        animateGradient();
      });
    };
    animateGradient();
  }, []);

  const currentColorIndex = Math.floor(gradientAnim._value * colors.length);
  const nextColorIndex = (currentColorIndex + 1) % colors.length;
  const progress = (gradientAnim._value * colors.length) % 1;

  const interpolatedColors = colors[currentColorIndex].map((color, index) => {
    const nextColor = colors[nextColorIndex][index];
    return interpolateColor(color, nextColor, progress);
  });

  return (
    <View style={styles.container}>
      <LinearGradient
        colors={interpolatedColors}
        style={styles.gradient}
        start={{ x: 0, y: 0 }}
        end={{ x: 1, y: 1 }}
      >
        <View style={styles.content}>
          {/* Logo/App Name */}
          <View style={styles.logoContainer}>
            <Text style={styles.logo}>WASTE</Text>
            <Text style={styles.logoSub}>SORT</Text>
          </View>

          {/* Animated Quote */}
          <Animated.View
            style={[
              styles.quoteContainer,
              {
                opacity: fadeAnim,
                transform: [{ translateY: slideAnim }],
              },
            ]}
          >
            <Text style={styles.quote}>
              {quotes[currentColorIndex]}
            </Text>
          </Animated.View>

          {/* Get Started Button */}
          <TouchableOpacity
            style={styles.button}
            onPress={() => router.push('/(tabs)/explore')}
            activeOpacity={0.8}
          >
            <Text style={styles.buttonText}>Get Started</Text>
          </TouchableOpacity>
        </View>
      </LinearGradient>
    </View>
  );
}

// Helper function to interpolate colors
function interpolateColor(color1, color2, factor) {
  const result = color1.match(/\d+/g).map((start, i) => {
    const end = color2.match(/\d+/g)[i];
    const startNum = parseInt(start);
    const endNum = parseInt(end);
    const resultNum = Math.round(startNum + factor * (endNum - startNum));
    return resultNum;
  });
  return `rgb(${result[0]}, ${result[1]}, ${result[2]})`;
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  gradient: {
    flex: 1,
  },
  content: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    paddingHorizontal: 40,
  },
  logoContainer: {
    alignItems: 'center',
    marginBottom: 60,
  },
  logo: {
    fontSize: 48,
    fontWeight: 'bold',
    color: 'white',
    letterSpacing: 2,
  },
  logoSub: {
    fontSize: 32,
    fontWeight: '300',
    color: 'white',
    letterSpacing: 4,
    marginTop: -10,
  },
  quoteContainer: {
    alignItems: 'center',
    marginBottom: 80,
  },
  quote: {
    fontSize: 24,
    color: 'white',
    textAlign: 'center',
    fontWeight: '300',
    lineHeight: 32,
    paddingHorizontal: 20,
  },
  button: {
    backgroundColor: 'white',
    paddingHorizontal: 40,
    paddingVertical: 16,
    borderRadius: 30,
    shadowColor: '#000',
    shadowOffset: {
      width: 0,
      height: 4,
    },
    shadowOpacity: 0.3,
    shadowRadius: 8,
    elevation: 8,
  },
  buttonText: {
    fontSize: 18,
    fontWeight: '600',
    color: '#333',
  },
});
