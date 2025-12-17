import xml.etree.ElementTree as ET
class SVGElement(ET.Element):
    def __init__(self, tag, attrib={}, text=None, **extra):
        super().__init__(tag, attrib, **extra)
        self.text = text

skeleton_plot = SVGElement(
    "svg",
    {
        "width": "256",
        "height": "144",
        "xmlns": "http://www.w3.org/2000/svg",
        "xmlns:xlink": "http://www.w3.org/1999/xlink",
        "viewBox": "0 0 256 144",
        "preserveAspectRatio": "xMinYMin meet",
    }
)

# Style
style = SVGElement(
    "link",
    {
        "xmlns": "http://www.w3.org/1999/xhtml",
        "rel": "stylesheet",
        "href": "skeleton.css",
        "type": "text/css",
    }
)

# Background
background = SVGElement(
    "rect",
    {
        "width": "100%",
        "height": "100%",
        "class": "background",
    }
)

# Panel
panel = SVGElement("g",{"class": "panel"})
panel.append(SVGElement(
    "rect",
    {
        "x": "20",
        "y": "16",
        "width": "208",
        "height": "112",
    }
))
panel.append(SVGElement(
    "text",
    {
        "x": "124",
        "y": "70",
        "font-size": "12"
    },
    "Panel"
))

# Plot title
plot_title = SVGElement("g",{"class": "plot-title"})
plot_title.append(SVGElement(
    "line",
    {
        "x1": "0%",
        "y1": "12",
        "x2": "100%",
        "y2": "12",
        "class": "guide-line",
    }
))
plot_title.append(SVGElement(
    "line",
    {
        "x1": "0%",
        "y1": "2",
        "x2": "100%",
        "y2": "2",
        "class": "guide-line",
    }
))
plot_title.append(
    SVGElement(
        "text",
        {
            "x": "128",
            "y": "12",
            "font-size": "10",
        },
        "Plot Title"
    )
)

# Vertical Axis Title
vertical_axis_title = SVGElement("g",{"class": "vertical-axis-title"})
vertical_axis_title.append(SVGElement(
    "line",
    { 
        "x1": "8",
        "y1": "0%",
        "x2": "8",
        "y2": "100%",
        "class": "guide-line",
    }
))
vertical_axis_title.append(SVGElement(
    "line",
    {
        "x1": "2",
        "y1": "0%",
        "x2": "2",
        "y2": "100%",
        "class": "guide-line",
    }
))
vertical_axis_title.append(SVGElement(
    "text",
    {
        "x": "8",
        "y": "72",
        "font-size": "6",
        "transform": "rotate(-90,8,72)",
    },
    "Vertical Axis Title"
))

# Horizontal Axis Title
horizontal_axis_title = SVGElement("g",{"class": "horizontal-axis-title"})
horizontal_axis_title.append(SVGElement(
    "line",
    { 
        "x1": "0%",
        "y1": "142",
        "x2": "100%",
        "y2": "142",
        "class": "guide-line",
    }
))
horizontal_axis_title.append(SVGElement(
    "line",
    {
        "x1": "0%",
        "y1": "136",
        "x2": "100%",
        "y2": "136",
        "class": "guide-line",
    }
))
horizontal_axis_title.append(SVGElement(
    "text",
    {
        "x": "124",
        "y": "142",
        "font-size": "6",
    },
    "Horizontal Axis Title"
))

# Put everything together
skeleton_plot.append(style)
skeleton_plot.append(background)
skeleton_plot.append(panel)
skeleton_plot.append(plot_title)
skeleton_plot.append(vertical_axis_title)
skeleton_plot.append(horizontal_axis_title)

# Tree
tree = ET.ElementTree(skeleton_plot)
ET.indent(tree, space="    ", level=0)
tree.write("public/blog/attachments/2025/11-Nov/2025-11-30/skeleton.svg")
