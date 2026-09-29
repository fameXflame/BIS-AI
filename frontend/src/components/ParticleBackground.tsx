'use client';

import { useEffect, useRef } from 'react';

interface ParticleBackgroundProps {
  theme?: 'light' | 'dark';
}

interface Node {
  x: number;
  y: number;
  vx: number;
  vy: number;
  radius: number;
  color: string;
  alpha: number;
}

export default function ParticleBackground({ theme = 'light' }: ParticleBackgroundProps) {
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const mouseRef = useRef<{ x: number | null; y: number | null }>({ x: null, y: null });

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    if (!ctx) return;

    let animationFrameId: number;
    let width = (canvas.width = window.innerWidth);
    let height = (canvas.height = window.innerHeight);

    const handleResize = () => {
      if (!canvas) return;
      width = canvas.width = window.innerWidth;
      height = canvas.height = window.innerHeight;
      initNodes();
    };

    window.addEventListener('resize', handleResize);

    const handleMouseMove = (e: MouseEvent) => {
      mouseRef.current = { x: e.clientX, y: e.clientY };
    };

    const handleMouseLeave = () => {
      mouseRef.current = { x: null, y: null };
    };

    window.addEventListener('mousemove', handleMouseMove);
    document.addEventListener('mouseleave', handleMouseLeave);

    // Color definitions for Knowledge Graph Nodes
    const isDark = theme === 'dark';
    const nodeColors = isDark
      ? [
          'rgba(59, 130, 246, ',   // Blue
          'rgba(96, 165, 250, ',   // Light Blue
          'rgba(14, 165, 233, ',   // Sky
          'rgba(148, 163, 184, ',  // Slate
        ]
      : [
          'rgba(37, 99, 235, ',    // Royal Blue
          'rgba(30, 64, 175, ',    // Deep Blue
          'rgba(100, 116, 139, ',  // Slate
          'rgba(79, 70, 229, ',    // Indigo
        ];

    let nodes: Node[] = [];
    const nodeCount = Math.min(Math.floor((width * height) / 14000), 75);
    const maxDistance = 120;
    const mouseDistance = 150;

    const initNodes = () => {
      nodes = [];
      for (let i = 0; i < nodeCount; i++) {
        const baseColor = nodeColors[Math.floor(Math.random() * nodeColors.length)];
        const alpha = isDark ? 0.35 + Math.random() * 0.35 : 0.25 + Math.random() * 0.3;
        nodes.push({
          x: Math.random() * width,
          y: Math.random() * height,
          vx: (Math.random() - 0.5) * 0.45,
          vy: (Math.random() - 0.5) * 0.45,
          radius: 1.8 + Math.random() * 2.2,
          color: baseColor,
          alpha,
        });
      }
    };

    initNodes();

    const render = () => {
      ctx.clearRect(0, 0, width, height);

      // 1. Draw connections between nearby nodes (Normative Graph Edges)
      for (let i = 0; i < nodes.length; i++) {
        for (let j = i + 1; j < nodes.length; j++) {
          const dx = nodes[i].x - nodes[j].x;
          const dy = nodes[i].y - nodes[j].y;
          const dist = Math.sqrt(dx * dx + dy * dy);

          if (dist < maxDistance) {
            const edgeAlpha = (1 - dist / maxDistance) * (isDark ? 0.16 : 0.11);
            ctx.beginPath();
            ctx.moveTo(nodes[i].x, nodes[i].y);
            ctx.lineTo(nodes[j].x, nodes[j].y);
            ctx.strokeStyle = isDark
              ? `rgba(96, 165, 250, ${edgeAlpha})`
              : `rgba(37, 99, 235, ${edgeAlpha})`;
            ctx.lineWidth = 0.85;
            ctx.stroke();
          }
        }

        // Connection to mouse cursor (Interactive Copilot Radar)
        if (mouseRef.current.x !== null && mouseRef.current.y !== null) {
          const mdx = nodes[i].x - mouseRef.current.x;
          const mdy = nodes[i].y - mouseRef.current.y;
          const mdist = Math.sqrt(mdx * mdx + mdy * mdy);

          if (mdist < mouseDistance) {
            const mAlpha = (1 - mdist / mouseDistance) * (isDark ? 0.28 : 0.18);
            ctx.beginPath();
            ctx.moveTo(nodes[i].x, nodes[i].y);
            ctx.lineTo(mouseRef.current.x, mouseRef.current.y);
            ctx.strokeStyle = isDark
              ? `rgba(59, 130, 246, ${mAlpha})`
              : `rgba(37, 99, 235, ${mAlpha})`;
            ctx.lineWidth = 1;
            ctx.stroke();
          }
        }
      }

      // 2. Draw nodes & update positions
      for (let i = 0; i < nodes.length; i++) {
        const node = nodes[i];

        node.x += node.vx;
        node.y += node.vy;

        // Bounce gently at screen borders
        if (node.x <= 0 || node.x >= width) node.vx *= -1;
        if (node.y <= 0 || node.y >= height) node.vy *= -1;

        ctx.beginPath();
        ctx.arc(node.x, node.y, node.radius, 0, Math.PI * 2);
        ctx.fillStyle = `${node.color}${node.alpha})`;
        ctx.fill();

        // Subtle glow halo for selected key standard nodes
        if (i % 5 === 0) {
          ctx.beginPath();
          ctx.arc(node.x, node.y, node.radius * 2.2, 0, Math.PI * 2);
          ctx.fillStyle = `${node.color}${node.alpha * 0.25})`;
          ctx.fill();
        }
      }

      animationFrameId = requestAnimationFrame(render);
    };

    render();

    return () => {
      cancelAnimationFrame(animationFrameId);
      window.removeEventListener('resize', handleResize);
      window.removeEventListener('mousemove', handleMouseMove);
      document.removeEventListener('mouseleave', handleMouseLeave);
    };
  }, [theme]);

  return (
    <canvas
      ref={canvasRef}
      className="absolute inset-0 w-full h-full pointer-events-none select-none"
      style={{ zIndex: 0 }}
    />
  );
}
