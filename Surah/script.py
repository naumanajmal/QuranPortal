from bs4 import BeautifulSoup
def has_data_or_non_empty_children(tag):
    # Check if the tag has any data value
    if tag.string and tag.string.strip():
        return True
    
    # Check if the tag has all empty children tags
    for child in tag.find_all(recursive=False):
        if child.string and child.string.strip():
            return True
    
    return False

def process_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    final_tags = []
    word_tags = ""
    for a_tag in soup.find_all('a'):
      a_tag.decompose()
    body_tag = soup.body
    outer_tags = [tag for tag in body_tag.find_all(recursive=False) if tag.parent == body_tag]
    # filtered_tags = [tag for tag in outer_tags if has_data_or_non_empty_children(tag)]
    for tag_index in range(0, len(outer_tags)-2, 2):
      print(tag_index)
      span_tags = outer_tags[tag_index].find_all('span')
      for tag in span_tags:
        if tag.string and '&nbsp;' in tag.string:
            # Check if '&nbsp;' is at the end of the tag data
            if tag.string.endswith('&nbsp;'):
                # Add the following tag to the previous tags
                word_tags = word_tags + str(tag)
                final_tags.append("<span>"+word_tags + "</span>")
                word_tags = ""
            else:
                final_tags.append("<span>"+word_tags + "</span>")
                word_tags = tag
        else:
            word_tags = word_tags + str(tag)
      if word_tags:
          final_tags.append("<span>"+word_tags + "</span>")
          word_tags = ""
        # print(index)
      print(final_tags)
      final_tags = []
      
      rows = outer_tags[tag_index+1].find_all('tr')
      first_row = rows[0].find_all('td')
      for cell in first_row:
         print(cell.get_text())
      second_row = rows[1].find('td').get_text()
      print(second_row)
    

# Example usage
html = '''<p class="c15 c7" dir="rtl"><span class="c11">فِئَ</span><span class="c9">ۃ</span><span class="c11">ٍ </span><span class="c10">&nbsp; &nbsp;</span><span class="c11">فَ</span><span class="c11 c14">ق</span><span class="c11">َ</span><span class="c11 c55">د</span><span class="c11">ۡ بَ</span><span class="c11 c23">ا</span><span class="c11">ٓءَ</span><span class="c10">&nbsp; &nbsp;</span><span class="c11">&nbsp;بِ</span><span class="c11 c14">غَض</span><span class="c11">َ</span><span class="c11 c44">بٍ</span><span class="c10">&nbsp; &nbsp;</span><span class="c11">&nbsp;</span><span class="c9">م</span><span class="c11">ِّنَ</span><span class="c10">&nbsp; &nbsp;</span><span class="c11">&nbsp;ا</span><span class="c11 c14">ل</span><span class="c11">لہِ </span><span class="c10">&nbsp; &nbsp; &nbsp;</span><span class="c11">وَمَاۡ</span><span class="c11 c82">و</span><span class="c11">ٰ</span><span class="c11 c44">ى</span><span class="c11">ہُ</span><span class="c10">&nbsp; &nbsp; &nbsp; </span><span class="c11">&nbsp;جَہَ</span><span class="c9">ن</span><span class="c11">َّمُ ؕ</span><span class="c10">&nbsp; &nbsp;</span><span class="c11">&nbsp;وَبِئۡسَ </span><span class="c10">&nbsp; &nbsp; &nbsp;</span><span class="c11">&nbsp;الۡمَ</span><span class="c11 c14">ص</span><span class="c11">ِ</span><span class="c11 c27">یۡر</span><span class="c17 c11">ُ </span></p>'''




with open('8.html', 'r') as file:
    html_content = file.read()

process_html(html_content)

