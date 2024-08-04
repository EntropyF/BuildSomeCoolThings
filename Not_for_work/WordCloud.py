import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Sample text
text = """
Description: TIPR has built out an Indicator Validation \\
Pipeline to evaluate threat intelligence IOCs, more specifically \\
to discern whether an indicator is a TP or FP based on product \\
telemetry. They are looking to build and improve their pipelines, \\
to eliminate hard-coded, arbitrary thresholds, and incorporate \\
SONAR product telemetry to build high fidelity validation pipelines.​
"""

# Generate word cloud
# wordcloud = WordCloud(width=800, height=400, background_color='black',
#                       colormap='viridis', contour_color='white',
#                       contour_width=3).generate(text)

wordcloud = WordCloud(width = 800, height = 400,
                background_color ='white',
                min_font_size = 10).generate(text)

# Display the word cloud using matplotlib
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
