"""
BIS AI — Compliance Dossier PDF Generator
==========================================
Generates a publication-grade, official Bureau of Indian Standards
Compliance Dossier & Audit Checklist PDF using ReportLab.
"""

import io
import os
from datetime import datetime
from typing import Dict, Any, List

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    KeepTogether,
    HRFlowable
)
from reportlab.pdfgen import canvas


class NumberedCanvas(canvas.Canvas):
    """Adds professional running header and page numbering footer."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_header_footer(num_pages)
            super().showPage()
        super().save()

    def draw_header_footer(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#64748b"))

        # Running Header (pages > 1)
        if self._pageNumber > 1:
            self.drawString(54, letter[1] - 36, "BIS AI Regulatory Intelligence — Compliance Dossier & Audit Checklist")
            self.setStrokeColor(colors.HexColor("#e2e8f0"))
            self.setLineWidth(0.5)
            self.line(54, letter[1] - 42, letter[0] - 54, letter[1] - 42)

        # Running Footer
        page_text = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(letter[0] - 54, 30, page_text)
        self.drawString(54, 30, "CONFIDENTIAL & PROPRIETARY — GENERATED VIA BIS AI COMPLIANCE ENGINE")
        self.setStrokeColor(colors.HexColor("#e2e8f0"))
        self.setLineWidth(0.5)
        self.line(54, 40, letter[0] - 54, 40)

        self.restoreState()


def generate_dossier_pdf(query: str, search_results: Dict[str, Any]) -> bytes:
    """
    Builds a vector PDF report for a query and its retrieved standards.
    """
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(
        buffer,
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54,
    )

    styles = getSampleStyleSheet()

    # Custom typography styles
    primary_color = colors.HexColor("#0f172a") # Slate 900
    brand_blue = colors.HexColor("#0284c7")    # Sky 600
    accent_dark = colors.HexColor("#1e293b")   # Slate 800
    subtle_text = colors.HexColor("#475569")   # Slate 600
    light_bg = colors.HexColor("#f8fafc")      # Slate 50
    border_color = colors.HexColor("#cbd5e1")  # Slate 300

    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=primary_color,
        spaceAfter=4
    )

    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=14,
        textColor=brand_blue,
        spaceAfter=12
    )

    h1_style = ParagraphStyle(
        'Heading1_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=accent_dark,
        spaceBefore=14,
        spaceAfter=6
    )

    body_style = ParagraphStyle(
        'Body_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=14,
        textColor=subtle_text,
    )

    meta_label_style = ParagraphStyle(
        'MetaLabel',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11,
        textColor=primary_color
    )

    meta_val_style = ParagraphStyle(
        'MetaVal',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11,
        textColor=subtle_text
    )

    std_code_style = ParagraphStyle(
        'StdCode',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=13,
        textColor=brand_blue
    )

    std_title_style = ParagraphStyle(
        'StdTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9,
        leading=12,
        textColor=primary_color
    )

    std_meta_style = ParagraphStyle(
        'StdMeta',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=11,
        textColor=subtle_text
    )

    story = []

    # 1. Header Block with Emblem and Title
    header_data = [
        [
            Paragraph("<b>BUREAU OF INDIAN STANDARDS</b><br/><font size=8 color='#64748b'>MANAK BHAVAN, NEW DELHI • AI REGULATORY INTELLIGENCE DIVISION</font>", ParagraphStyle('H1', fontName='Helvetica-Bold', fontSize=10, leading=13, textColor=primary_color)),
            Paragraph(f"<b>DOSSIER REF:</b> BIS-AI-{int(datetime.now().timestamp())}<br/><b>DATE:</b> {datetime.now().strftime('%d %b %Y, %H:%M')}", ParagraphStyle('H2', fontName='Helvetica', fontSize=8, leading=11, alignment=2, textColor=subtle_text))
        ]
    ]
    header_table = Table(header_data, colWidths=[330, 174])
    header_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(header_table)
    story.append(HRFlowable(width="100%", thickness=1.5, color=primary_color, spaceBefore=0, spaceAfter=14))

    # 2. Document Title
    story.append(Paragraph("STANDARDS COMPLIANCE DOSSIER & AUDIT ROADMAP", title_style))
    story.append(Paragraph("OFFICIAL REGULATORY BENCHMARK FOR INDUSTRIAL & COMMERCIAL CONFORMANCE", subtitle_style))
    story.append(Spacer(1, 8))

    # 3. Query & Metadata Summary Box
    summary_text = search_results.get("summary", "Analysis completed against Indian Standards repository.")
    magnified = search_results.get("query_magnified", query)
    standards: List[Dict[str, Any]] = search_results.get("standards", [])

    meta_box_data = [
        [Paragraph("Target Query / Requirement:", meta_label_style), Paragraph(f"<b>\"{query}\"</b>", meta_val_style)],
        [Paragraph("Semantic Magnification:", meta_label_style), Paragraph(magnified, meta_val_style)],
        [Paragraph("Corpus Coverage:", meta_label_style), Paragraph(f"1,002 Active National Standards (Civil, Electrical, Chemical, Mechanical, Transport, Electronics)", meta_val_style)],
        [Paragraph("Matches Identified:", meta_label_style), Paragraph(f"<b>{len(standards)} Relevant Standards</b> ({sum(1 for s in standards if s.get('mandatory'))} Mandatory / QCO)", meta_val_style)],
    ]
    meta_table = Table(meta_box_data, colWidths=[140, 364])
    meta_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), light_bg),
        ('BOX', (0,0), (-1,-1), 0.5, border_color),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#e2e8f0")),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(meta_table)
    story.append(Spacer(1, 14))

    # 4. Executive Summary
    story.append(Paragraph("1. Executive Regulatory Overview", h1_style))
    story.append(Paragraph(summary_text, body_style))
    story.append(Spacer(1, 10))

    # 5. AI Walkalong / Advisory if present
    walkalong = search_results.get("ai_walkalong")
    if walkalong:
        story.append(Paragraph("2. Strategic Compliance Walk-Along Advisory", h1_style))
        walkalong_cleaned = walkalong.replace("\n", "<br/>")
        story.append(Paragraph(walkalong_cleaned, body_style))
        story.append(Spacer(1, 10))

    # 6. Applicable Indian Standards Matrix
    story.append(Paragraph("3. Applicable Indian Standards Matrix", h1_style))

    table_rows = [
        [
            Paragraph("<b>IS Code</b>", meta_label_style),
            Paragraph("<b>Standard Title & Technical Scope</b>", meta_label_style),
            Paragraph("<b>Status / QCO</b>", meta_label_style),
            Paragraph("<b>Match</b>", meta_label_style)
        ]
    ]

    for std in standards[:8]: # Top 8 most relevant
        code = std.get("is_code", "")
        title = std.get("title", "")
        scope = std.get("abstract_scope") or std.get("highlight_reason") or std.get("scope", "")
        if len(scope) > 180:
            scope = scope[:177] + "..."
        division = std.get("division", "BIS")
        mandatory = "<b>MANDATORY (QCO)</b>" if std.get("mandatory") else "Voluntary"
        confidence = f"{std.get('confidence', 85)}%"

        cell_title = Paragraph(f"<font color='#0284c7'><b>{title}</b></font><br/><font size=7.5 color='#475569'>{scope}</font><br/><font size=7 color='#94a3b8'>Division: {division}</font>", std_meta_style)
        cell_code = Paragraph(f"<b>{code}</b>", std_code_style)
        cell_status = Paragraph(f"<font color=\"{'#b91c1c' if std.get('mandatory') else '#475569'}\">{mandatory}</font>", meta_val_style)
        cell_conf = Paragraph(f"<b>{confidence}</b>", meta_val_style)

        table_rows.append([cell_code, cell_title, cell_status, cell_conf])

    std_table = Table(table_rows, colWidths=[90, 274, 90, 50])
    std_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#0f172a")),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOX', (0,0), (-1,-1), 0.5, border_color),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#e2e8f0")),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    # Header text colors
    std_table.setStyle(TableStyle([
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ]))
    story.append(std_table)
    story.append(Spacer(1, 14))

    # 7. Step-by-Step BIS Certification Roadmap & Testing Checklist
    story.append(Paragraph("4. Step-by-Step BIS Certification Audit Roadmap", h1_style))

    roadmap_data = [
        [
            Paragraph("<b>Stage</b>", meta_label_style),
            Paragraph("<b>Operational Milestone</b>", meta_label_style),
            Paragraph("<b>Verification Requirement</b>", meta_label_style)
        ],
        [
            Paragraph("Phase 1", meta_label_style),
            Paragraph("<b>Standard Identification & Gap Analysis</b>", std_title_style),
            Paragraph("Procure official standard specification; verify testing equipment in in-house lab meets specified tolerances.", body_style)
        ],
        [
            Paragraph("Phase 2", meta_label_style),
            Paragraph("<b>Form-IV Online Application (e-BIS)</b>", std_title_style),
            Paragraph("Submit manufacturing layout, test machinery calibration certificates, and raw material vendor test certificates.", body_style)
        ],
        [
            Paragraph("Phase 3", meta_label_style),
            Paragraph("<b>Factory Audit & Independent Sampling</b>", std_title_style),
            Paragraph("BIS Inspecting Officer verifies quality control personnel, draws duplicate samples for third-party NABL lab testing.", body_style)
        ],
        [
            Paragraph("Phase 4", meta_label_style),
            Paragraph("<b>Grant of Standard Mark (ISI / CRS)</b>", std_title_style),
            Paragraph("Upon test clearance, pay marking fee; print valid CML / Registration number and ISI logo on primary packaging.", body_style)
        ],
    ]
    roadmap_table = Table(roadmap_data, colWidths=[60, 180, 264])
    roadmap_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), light_bg),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOX', (0,0), (-1,-1), 0.5, border_color),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#e2e8f0")),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(roadmap_table)
    story.append(Spacer(1, 14))

    # 8. Sign-off Disclaimer
    disclaimer = Paragraph(
        "<font size=7 color='#94a3b8'><b>DISCLAIMER:</b> This dossier is generated by the BIS AI Search & Compliance Intelligence Platform for preliminary informational and regulatory pre-audit screening. Manufacturers and exporters must cross-reference official Gazette Notifications and Quality Control Orders (QCOs) published by the Ministry of Consumer Affairs and the Bureau of Indian Standards at manakonline.in.</font>",
        body_style
    )
    story.append(KeepTogether([disclaimer]))

    # Build document
    doc.build(story, canvasmaker=NumberedCanvas)
    buffer.seek(0)
    return buffer.getvalue()
