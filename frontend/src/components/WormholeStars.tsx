'use client';

import { useEffect, useRef } from 'react';

interface Star {
  x: number;
  y: number;
  z: number;
  pz: number;
  color: number;
}

export default function WormholeStars() {
  const canvasRef = useRef<HTMLCanvasElement>(null);

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    if (!ctx) return;

    let animationId: number;
    const stars: Star[] = [];
    const STAR_COUNT = 500;
    const BASE_SPEED = 1.5;

    // Color palette for star tints [r, g, b]
    const palette = [
      [255, 255, 255],   // pure white
      [255, 255, 255],   // pure white (weighted)
      [186, 230, 253],   // sky-200
      [196, 181, 253],   // violet-300
      [165, 243, 252],   // cyan-200
      [253, 230, 138],   // amber-200 (rare warm star)
    ];

    const resize = () => {
      canvas.width = window.innerWidth;
      canvas.height = window.innerHeight;
    };

    const createStar = (): Star => ({
      x: (Math.random() - 0.5) * canvas.width * 1.5,
      y: (Math.random() - 0.5) * canvas.height * 1.5,
      z: Math.random() * canvas.width,
      pz: 0,
      color: Math.floor(Math.random() * palette.length),
    });

    const initStars = () => {
      stars.length = 0;
      for (let i = 0; i < STAR_COUNT; i++) {
        const s = createStar();
        s.pz = s.z;
        stars.push(s);
      }
    };

    const draw = () => {
      // Trail effect: semi-transparent black fill
      ctx.fillStyle = 'rgba(0, 0, 0, 0.12)';
      ctx.fillRect(0, 0, canvas.width, canvas.height);

      const cx = canvas.width / 2;
      const cy = canvas.height / 2;
      const maxDim = Math.max(canvas.width, canvas.height);

      for (let i = 0; i < stars.length; i++) {
        const star = stars[i];
        star.pz = star.z;
        star.z -= BASE_SPEED;

        if (star.z <= 1) {
          stars[i] = createStar();
          stars[i].pz = stars[i].z;
          continue;
        }

        // Project current position
        const sx = (star.x / star.z) * (maxDim * 0.5) + cx;
        const sy = (star.y / star.z) * (maxDim * 0.5) + cy;

        // Skip if off screen
        if (sx < -50 || sx > canvas.width + 50 || sy < -50 || sy > canvas.height + 50) {
          continue;
        }

        // Project previous position for trail
        const px = (star.x / star.pz) * (maxDim * 0.5) + cx;
        const py = (star.y / star.pz) * (maxDim * 0.5) + cy;

        // Size and opacity based on depth
        const depthRatio = 1 - star.z / canvas.width;
        const size = Math.max(0.3, depthRatio * 2.5);
        const opacity = Math.max(0.05, depthRatio * 0.7);

        const [r, g, b] = palette[star.color];

        // Draw trail line
        ctx.beginPath();
        ctx.moveTo(px, py);
        ctx.lineTo(sx, sy);
        ctx.strokeStyle = `rgba(${r}, ${g}, ${b}, ${opacity * 0.6})`;
        ctx.lineWidth = size * 0.4;
        ctx.stroke();

        // Draw star dot
        ctx.beginPath();
        ctx.arc(sx, sy, size * 0.45, 0, Math.PI * 2);
        ctx.fillStyle = `rgba(${r}, ${g}, ${b}, ${opacity})`;
        ctx.fill();
      }

      // Subtle central vortex glow
      const grad = ctx.createRadialGradient(cx, cy, 0, cx, cy, maxDim * 0.25);
      grad.addColorStop(0, 'rgba(99, 102, 241, 0.018)');
      grad.addColorStop(0.4, 'rgba(139, 92, 246, 0.008)');
      grad.addColorStop(1, 'rgba(0, 0, 0, 0)');
      ctx.fillStyle = grad;
      ctx.fillRect(0, 0, canvas.width, canvas.height);

      animationId = requestAnimationFrame(draw);
    };

    resize();
    initStars();
    draw();

    const handleResize = () => {
      resize();
      initStars();
    };
    window.addEventListener('resize', handleResize);

    return () => {
      cancelAnimationFrame(animationId);
      window.removeEventListener('resize', handleResize);
    };
  }, []);

  return (
    <canvas
      ref={canvasRef}
      className="fixed inset-0 z-0 pointer-events-none"
      style={{ background: '#000000' }}
    />
  );
}
