'use client';

import { useEffect, useRef } from 'react';

export default function ParticleBackground() {
  const containerRef = useRef<HTMLDivElement>(null);
  const scriptRef = useRef<HTMLScriptElement | null>(null);

  useEffect(() => {
    // Dynamically load the particle system script
    if (!scriptRef.current) {
      const script = document.createElement('script');
      script.type = 'module';
      script.src = '/_astro/MainParticlesComponent.astro_astro_type_script_index_0_lang.ZV8AJEPG.js';
      document.body.appendChild(script);
      scriptRef.current = script;
    }

    return () => {
      // Cleanup: remove canvases from the container on unmount
      if (containerRef.current) {
        const canvases = containerRef.current.querySelectorAll('canvas');
        canvases.forEach((c) => c.remove());
      }
      if (scriptRef.current) {
        scriptRef.current.remove();
        scriptRef.current = null;
      }
    };
  }, []);

  return (
    <div
      className="main-particles-component-section"
      data-main-particles-component
      data-theme="light"
      data-ring-width="0.006"
      data-ring-width2="0.107"
      data-ring-displacement="0.62"
      data-density="230"
      data-particles-scale="0.59"
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
