im_list = ['в', '7', 'часов', '7', 'минут', 'температура', 'воздуха', 'была', '+55', 'градусов']
for i in range(0, len(im_list)):
    if im_list[i].isdigit():
        if int(im_list[i]) < 10:
            im_list.insert(i, '0' + im_list[i])
            im_list.remove(im_list[i + 1])
line = ' '.join(im_list)
c = line.find('+')
if line[c+2].isdigit() == True:
    x = line[c+1] + line[c+2]
else:
    x = f'{int(line[c+1]):02d}'
im_list[8] = x
line = ' '.join(im_list)
print(line)
