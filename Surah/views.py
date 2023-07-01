from django.http import HttpResponse
from django.shortcuts import render
from django.http import FileResponse
from .models import *
from bs4 import BeautifulSoup
import re
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json



def index(request):
  surahs = [
    {'id': 1, 'name': 'Al-Fatiha'},
    {'id': 2, 'name': 'Al-Baqarah'},
    {'id': 3, 'name': 'Aal-E-Imran'},
    {'id': 4, 'name': 'An-Nisa'},
    {'id': 5, 'name': 'Al-Maeda'},
    {'id': 6, 'name': 'Al-Anam'},
    {'id': 7, 'name': 'Al-Araf'},
    {'id': 8, 'name': 'Al-Anfal'},
    {'id': 9, 'name': 'At-Tawba'},
    {'id': 10, 'name': 'Yunus'},
    {'id': 11, 'name': 'Hud'},
    {'id': 12, 'name': 'Yusuf'},
    {'id': 13, 'name': 'Ar-Rad'},
    {'id': 14, 'name': 'Ibrahim'},
    {'id': 15, 'name': 'Al-Hijr'},
    {'id': 16, 'name': 'An-Nahl'},
    {'id': 17, 'name': 'Al-Isra'},
    {'id': 18, 'name': 'Al-Kahf'},
    {'id': 19, 'name': 'Maryam'},
    {'id': 20, 'name': 'Ta-Ha'},
    {'id': 21, 'name': 'Al-Anbiya'},
    {'id': 22, 'name': 'Al-Hajj'},
    {'id': 23, 'name': 'Al-Mumenoon'},
    {'id': 24, 'name': 'An-Noor'},
    {'id': 25, 'name': 'Al-Furqan'},
    {'id': 26, 'name': 'Ash-Shuara'},
    {'id': 27, 'name': 'An-Naml'},
    {'id': 28, 'name': 'Al-Qasas'},
    {'id': 29, 'name': 'Al-Ankaboot'},
    {'id': 30, 'name': 'Ar-Room'},
    {'id': 31, 'name': 'Luqman'},
    {'id': 32, 'name': 'As-Sajda'},
    {'id': 33, 'name': 'Al-Ahzab'},
    {'id': 34, 'name': 'Saba'},
    {'id': 35, 'name': 'Fatir'},
    {'id': 36, 'name': 'Ya-Seen'},
    {'id': 37, 'name': 'As-Saaffat'},
    {'id': 38, 'name': 'Sad'},
    {'id': 39, 'name': 'Az-Zumar'},
    {'id': 40, 'name': 'Ghafir'},
    {'id': 41, 'name': 'Fussilat'},
    {'id': 42, 'name': 'Ash-Shura'},
    {'id': 43, 'name': 'Az-Zukhruf'},
    {'id': 44, 'name': 'Ad-Dukhan'},
    {'id': 45, 'name': 'Al-Jathiya'},
    {'id': 46, 'name': 'Al-Ahqaf'},
    {'id': 47, 'name': 'Muhammad'},
    {'id': 48, 'name': 'Al-Fath'},
    {'id': 49, 'name': 'Al-Hujurat'},
    {'id': 50, 'name': 'Qaf'},
    {'id': 51, 'name': 'Adh-Dhariyat'},
    {'id': 52, 'name': 'At-Tur'},
    {'id': 53, 'name': 'An-Najm'},
    {'id': 54, 'name': 'Al-Qamar'},
    {'id': 55, 'name': 'Ar-Rahman'},
    {'id': 56, 'name': 'Al-Waqia'},
    {'id': 57, 'name': 'Al-Hadid'},
    {'id': 58, 'name': 'Al-Mujadila'},
    {'id': 59, 'name': 'Al-Hashr'},
    {'id': 60, 'name': 'Al-Mumtahina'},
    {'id': 61, 'name': 'As-Saff'},
    {'id': 62, 'name': 'Al-Jumuah'},
    {'id': 63, 'name': 'Al-Munafiqoon'},
    {'id': 64, 'name': 'At-Taghabun'},
    {'id': 65, 'name': 'At-Talaq'},
    {'id': 66, 'name': 'At-Tahrim'},
    {'id': 67, 'name': 'Al-Mulk'},
    {'id': 68, 'name': 'Al-Qalam'},
    {'id': 69, 'name': 'Al-Haaqqa'},
    {'id': 70, 'name': 'Al-Maarij'},
    {'id': 71, 'name': 'Nooh'},
    {'id': 72, 'name': 'Al-Jinn'},
    {'id': 73, 'name': 'Al-Muzzammil'},
    {'id': 74, 'name': 'Al-Muddathir'},
    {'id': 75, 'name': 'Al-Qiyama'},
    {'id': 76, 'name': 'Al-Insan'},
    {'id': 77, 'name': 'Al-Mursalat'},
    {'id': 78, 'name': 'An-Naba'},
    {'id': 79, 'name': 'An-Nazi-at'},
    {'id': 80, 'name': 'Abasa'},
    {'id': 81, 'name': 'At-Takwir'},
    {'id': 82, 'name': 'Al-Infitar'},
    {'id': 83, 'name': 'Al-Mutaffifin'},
    {'id': 84, 'name': 'Al-Inshiqaq'},
    {'id': 85, 'name': 'Al-Burooj'},
    {'id': 86, 'name': 'At-Tariq'},
    {'id': 87, 'name': 'Al-Ala'},
    {'id': 88, 'name': 'Al-Ghashiyah'},
    {'id': 89, 'name': 'Al-Fajr'},
    {'id': 90, 'name': 'Al-Balad'},
    {'id': 91, 'name': 'Ash-Shams'},
    {'id': 92, 'name': 'Al-Lail'},
    {'id': 93, 'name': 'Ad-Duha'},
    {'id': 94, 'name': 'Ash-Sharh'},
    {'id': 95, 'name': 'At-Tin'},
    {'id': 96, 'name': 'Al-Alaq'},
    {'id': 97, 'name': 'Al-Qadr'},
    {'id': 98, 'name': 'Al-Bayyina'},
    {'id': 99, 'name': 'Az-Zalzalah'},
    {'id': 100, 'name': 'Al-Adiyat'},
    {'id': 101, 'name': 'Al-Qaria'},
    {'id': 102, 'name': 'At-Takathur'},
    {'id': 103, 'name': 'Al-Asr'},
    {'id': 104, 'name': 'Al-Humaza'},
    {'id': 105, 'name': 'Al-Fil'},
    {'id': 106, 'name': 'Quraish'},
    {'id': 107, 'name': 'Al-Maun'},
    {'id': 108, 'name': 'Al-Kawthar'},
    {'id': 109, 'name': 'Al-Kafiroon'},
    {'id': 110, 'name': 'An-Nasr'},
    {'id': 111, 'name': 'Al-Masad'},
    {'id': 112, 'name': 'Al-Ikhlas'},
    {'id': 113, 'name': 'Al-Falaq'},
    {'id': 114, 'name': 'An-Nas'}
]
  data = []
  ayat_objects = Ayat.objects.all()
  print(ayat_objects.count())

  for ayat in ayat_objects:
    word_objects = Word.objects.filter(ayat=ayat)
    arabic_list = [word.arabic for word in word_objects]
    urdu_list = [word.urdu for word in word_objects]
    ayat_data = {
        "translation": ayat.urdu,
        "id":ayat.id,
        "arabic": arabic_list,
        "english": urdu_list
    }
    print(ayat_data)
    data.append(ayat_data)
  context = {
        'ayats': data,
        'surahs':surahs
    }
  return render(request, 'main.html', context)


 
# views.py



def update_row(request, row_id):
    ayat = Ayat.objects.get(pk=row_id)
    words = Word.objects.filter(ayat=ayat)

    if request.method == 'POST':
        for word in words:
            new_arabic = request.POST.get(f'arabic_{word.id}')
            word.arabic = new_arabic
            word.save()
        return HttpResponse('Arabic words updated successfully!')

    context = {
        'ayat': ayat,
        'words': words[::-1],
    }
    return render(request, 'updateTable.html', context)
        






def main(request):
  new_surah = Surah(number = 8, arabic="سُوۡرَۃُ  الۡاَنۡفَالِ مَدَنِیَّۃٌ", urdu="سورہ الانفال مدینہ", english = "Al-Anfal")
  new_surah.save()
  with open('8.html', 'r') as file:
    html_content = file.read()
  process_html(html_content, new_surah)
  return render(request, 'empty.html')



def process_html(html, surah):
    ayats = []
    soup = BeautifulSoup(html, 'html.parser')
    final_tags = []
    
    for a_tag in soup.find_all('a'):
      a_tag.decompose()
    body_tag = soup.body
    outer_tags = [tag for tag in body_tag.find_all(recursive=False) if tag.parent == body_tag]
    # filtered_tags = [tag for tag in outer_tags if has_data_or_non_empty_children(tag)]
    for tag_index in range(0, len(outer_tags)-2, 2):
      word_tags = ""
      ayat_single = {}
      span_tags = outer_tags[tag_index].find_all('span')
    
      for index,  tag in enumerate(span_tags):
        if tag.string and tag.string.count("\xa0")>1:
            # Check if '&nbsp;' is at the end of the tag data
            if tag.string.count("\xa0")>1 and re.match(r"^[\xa0\s]*$", tag.string):
                # Add the following tag to the previous tags
                word_tags += str(tag) 
                # final_tags.append("<span>"+word_tags + "</span>")
                if word_tags:
                 final_tags.append(word_tags)
                word_tags = ""
            else:
                word_tags += str(tag)
               
        else:
            word_tags += str(tag)
      if word_tags:
          # final_tags.append("<span>"+word_tags + "</span>")
          final_tags.append(word_tags)
          word_tags = ""
        # print(index)
      
      ayat_single["arabic"] = final_tags[::-1]
      final_tags = []
      
      rows = outer_tags[tag_index+1].find_all('tr')
      first_row = rows[0].find_all('td')
      urdu_word_text = []
      for cell in first_row:
          urdu_word_text.append(cell.get_text())
      ayat_single["english"] = urdu_word_text[::-1]
      second_row = rows[1].find('td').get_text()
      ayat_single["translation"] = second_row
      ayats.append(ayat_single)
      print(ayat_single)
    for aya_index,  aya in enumerate(ayats):
         print(aya_index)
         ayat_obj = Ayat(number=aya_index + 1, surah=surah, urdu=aya["translation"])
         ayat_obj.save()
         for urdu_index, urd in enumerate(aya["english"]):
            word = Word(number=urdu_index + 1, ayat=ayat_obj, arabic=aya["arabic"][urdu_index] if urdu_index >= 0 and urdu_index < len(aya["arabic"]) else "", urdu=urd)
            word.save()

       
    return ayats


      
        
           
           
           