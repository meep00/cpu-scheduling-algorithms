import numpy as np
from process_generator import show_something


#Ten plik zawiera implementację algorytmów FIFO i LRU

#funkcje przyjmują sekwencję (listę) odwoływań do stron, i liczbę ramek pamięci
#funkcje zwracają liczbę zamian stron
class Page:
    def __init__(self, page_number, time_used = 0):
        self.page_number = page_number
        self.time_used = time_used

 
def generate_seq_of_pages_binomial(low, high, num_pages):
    pages = []

    avg = (high - low)/2
    p = 0.5  
    n = 2 * avg
    page_numbers = np.random.binomial(n, p, num_pages)

    #show_something(page_numbers)

    for i in range(num_pages):
        pages.append(page_numbers[i])

    return pages

def fifo(page_sequence, frame_size):
    frames = []
    offset_count = 0

    for page_number in page_sequence:
        #sprawdza czy jest strona w pamięci
        if page_number not in [page.page_number for page in frames] :
            #jeżeli nie ma, to dodajemy ją
            if len(frames) < frame_size:
                frames.append(Page(page_number))
            else:
                # nie ma miejsca. zwalniamy ramkkę, ktora była najdawniej załadowana
                frames.pop(0)
                frames.append(Page(page_number))
                offset_count += 1

    return offset_count

def lru(page_sequence, frame_size):
    frames = []
    offset_count = 0
    time = 1

    for page_number in page_sequence:
        #sprawdza czy jest strona w pamięci
        if page_number not in [page.page_number for page in frames] :
            #jeżeli nie ma, to dodajemy ją
            if len(frames) < frame_size:
                frames.append(Page(page_number, time_used= time))

            
            else:
                # nie ma miejsca. zwalniamy ramkę, ktora była najdawniej używana
                oldest_frame = min(frames, key=lambda page: page.time_used)
                oldest_frame_index = frames.index(oldest_frame)
                frames.remove(oldest_frame)
                frames.insert(oldest_frame_index, Page(page_number, time_used= time))
                offset_count += 1
            

        else: 
            #strona jest już w pamięci. Odnowiamy time_used
            for page in frames:
                if page.page_number == page_number:
                    page.time_used = time
                    break

        time+=1    

    return offset_count
