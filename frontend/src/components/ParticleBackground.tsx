'use client';

import { useEffect, useRef } from 'react';

interface ParticleBackgroundProps {
  theme?: 'light' | 'dark';
}

export default function ParticleBackground({ theme = 'light' }: ParticleBackgroundProps) {
  const containerRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const triggerInit = () => {
      setTimeout(() => {
        document.dispatchEvent(new Event('DOMContentLoaded'));
      }, 80);
    };

    const existingScript = document.querySelector('script[src*="MainParticlesComponent"]');
    if (existingScript) {
      triggerInit();
    } else {
      const script = document.createElement('script');
      script.type = 'module';
      script.src = '/_astro/MainParticlesComponent.astro_astro_type_script_index_0_lang.ZV8AJEPG.js';
      script.onload = triggerInit;
      document.body.appendChild(script);
    }

    return () => {
      if (containerRef.current) {
        const canvases = containerRef.current.querySelectorAll('canvas');
        canvases.forEach((c) => c.remove());
      }
    };
  }, [theme]);

  return (
    <div
      key={theme}
      className="main-particles-component-section"
      data-main-particles-component
      data-theme={theme}
      data-ring-width="0.006"
      data-ring-width2="0.107"
      data-ring-displacement="0.48"
      data-density="230"
      data-particles-scale="0.52"
      style={{
        width: '100%',
        height: '100%',
        position: 'absolute',
        top: 0,
        left: 0,
        overflow: 'hidden',
        zIndex: 0,
      }}
    >
      <div
        ref={containerRef}
        className="main-particles-container"
        data-container
        style={{
          width: '100%',
          height: '100%',
          position: 'absolute',
          top: 0,
          left: 0,
        }}
      />
    </div>
  );
}
