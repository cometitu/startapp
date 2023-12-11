# Import mimetypes module
import mimetypes
import os
import random

from django.conf import settings
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.db.models import F
from django.http import HttpResponse, FileResponse, JsonResponse


# Reportlab
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import io
import uuid
import random
from .models import Website, PageVisit


from localStoragePy import localStoragePy
localStorage = localStoragePy('local.store.app', 'text')


# Create your views here.
def intro(request):
    
    context ={   
        "urlLink" :"http://app1.res50.itu.dk/instruction", 
    }

    return render(request, 'mainapp/intro.html', context)



def instruction(request):
    urls = Website.objects.all().filter(total_count__lte=130).values()
    if urls:
        urlselected = random.choice(urls)
        urls.filter(url_name=urlselected["url_name"]).update(total_count = F("total_count") + 1)
        var_selected = urlselected["url_name"]
        code_name = urlselected["code_name"] 
    else:
        var_selected = "Admin"
        code_name = "None"
    
    if code_name == "APP2":
        st_code = "INFO"
    elif code_name == "APP3":
        st_code = "UND"
    elif code_name == "APP8":
        st_code = "BAS"
    elif code_name == "APP9":
        st_code = "DEF"
    elif code_name == "APP4":
        st_code = "ALL"
    else:
        return redirect('mainapp:errorpage')
    
    context ={   
        "st_code":st_code,
        "urlselected" : var_selected,
        "code_name": code_name,
    }
    return render(request, 'mainapp/instruction.html', context)



def instruction2(request):
    context ={   
    
    }
    return render(request, 'mainapp/instruction2.html', context)



def results(request):
    context ={   
    }
    return render(request, 'mainapp/results.html', context)




# Election information
def faq(request):
    
    context = { 
           
    }
    return render(request, 'mainapp/faq.html', context)


def info(request):
    
    context = { 
    
    }
    return render(request, 'mainapp/info.html', context)


def privacy(request):
    context = {
    }
    return render(request, 'mainapp/privacy.html', context)




def errorpage(request):
    context ={   
    }
    return render(request, 'mainapp/errorpage.html', context)



def tech_doc(request):
    context ={   
    }
    return render(request, 'mainapp/extrack/documentation.heliosvoting.org/index.html', context)


def tech_attack(request):
    context ={   
    }
    return render(request, 'mainapp/extrack/documentation.heliosvoting.org/attacks-and-defenses.html', context)


def tech_install(request):
    context ={   
    }
    return render(request, 'mainapp/extrack/documentation.heliosvoting.org/install.html', context)


def tech_ver1(request):
    context ={   
    }
    return render(request, 'mainapp/extrack/documentation.heliosvoting.org/verification-specs/helios-v1-and-v2-verification-specs.html', context)


def tech_ver3(request):
    context ={   
    }
    return render(request, 'mainapp/extrack/documentation.heliosvoting.org/verification-specs/helios-v3-verification-specs.html', context)


def tech_ver4(request):
    context ={   
    }
    return render(request, 'mainapp/extrack/documentation.heliosvoting.org/verification-specs/helios-v4.html', context)


def tech_mixnet(request):
    context ={   
    }
    return render(request, 'mainapp/extrack/documentation.heliosvoting.org/verification-specs/mixnet-support.html', context)





def download_file(request):
    #Get candidates to vote for the
    BC = ["Trisha Nunn","Bullock Mason","Chantel Origi"]
    BS = ["Hans Sapei","Ben Cassie","Vannesa Toffic"]
    
    BC_SELECT = random.choice(BC)
    BS_SELECT = random.choice(BS)
    
    
    # Create a file-like buffer to receive PDF data
    output = io.BytesIO()

    # Create the PDF object, using the buffer as its "file"
    p = canvas.Canvas(output, pagesize=letter)

    # Get dynamic content from the request or other sources
    title = request.GET.get('title', 'SECURE E2E INTERNET VOTING')

    # # Start writing the PDF content
    p.setFont("Helvetica-Bold", 18)
    
    # Calculate the center coordinates for the page
    page_width, page_height = letter
    text_width = p.stringWidth(title, "Helvetica-Bold", 18)
    center_x = (page_width - text_width) / 2
    center_y = page_height / 2

    # Center the text on the page
    p.drawCentredString(center_x + 120, 750, title)
    


    p.setFont("Helvetica-Bold", 14)
    p.drawString(30, 710, 'Study Instructions:')
    
    # Add more dynamic content as needed
    
    # Start writing the PDF content
    p.setFont("Helvetica", 12)
    p.drawString(30, 680, 'For the purpose of this study, you are a board member about to vote online in the board election.')
    
    p.setFont("Helvetica", 12)
    p.drawString(30, 660, 'Your task in this study is to cast your vote for your preferred candidate for the Board Chairperson')

    p.setFont("Helvetica", 12)
    p.drawString(30, 640, 'and Board Secretary positions.')
 
    
    #p.setFont("Helvetica-Bold", 12)
    #p.drawString(30, 630, 'Board Chairperson : ' + BC_SELECT)
    #p.setFont("Helvetica-Bold", 12)
    #p.drawString(30, 610, 'Board Secretary : ' + BS_SELECT)
    
    
    
    p.setFont("Helvetica", 12)
    p.drawString(30, 610, 'During the voting, you will be asked to authenticate using the credentials shown to you in the')
    p.setFont("Helvetica", 12)
    p.drawString(30, 590, 'the voting interface. Note, in a real-world elections the credentials will be issued to you separately')
    p.setFont("Helvetica", 12)
    p.drawString(30, 570, 'using secure communication channels and will not be displayed anywhere in the system.')
    

    
    # ...

    # Close the PDF object cleanly and finish the document
    p.showPage()
    p.save()

    # Generate a unique file name
    file_name = str(uuid.uuid4()) + '.pdf'

    # Set the appropriate response headers
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="{}"'.format(file_name)

    # Write the PDF file to the response
    output.seek(0)
    response.write(output.getvalue())
    
    return response



@csrf_exempt  # Disable CSRF protection for simplicity (you can enable it with proper configuration)
def track_page(request):
    if request.method == 'POST':
        page_name = request.POST.get('page_name')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        duration = request.POST.get('duration')
        
        # Convert duration to seconds
        duration_seconds = int(duration) // 1000
        print(duration)
        print(duration_seconds)

        # Create a new PageVisit object and save it to the database
        PageVisit.objects.create(
            page_name=page_name,
            start_time=start_time,
            end_time=end_time,
            duration=duration_seconds
        )

        return JsonResponse({'message': 'Time recorded successfully.'})

    return JsonResponse({'error': 'Invalid request method.'}, status=400)
