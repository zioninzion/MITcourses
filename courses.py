import random
easy = [('1', 'Civil and Environmental Engineering'), ('2', 'Mechanical Engineering'), ('3', 'Materials Science and Engineering'), ('4', 'Architecture'), ('5', 'Chemistry'), ('6', 'Electrical Engineering and Computer Science'), ('7', 'Biology'), ('8', 'Physics'), ('9', 'Brain and Cognitive Sciences'), ('10', 'Chemical Engineering'), ('11', 'Urban Studies and Planning'), ('12', 'Earth, Atmospheric, and Planetary Sciences'), ('14', 'Economics'), ('15', 'Management'), ('16', 'Aeronautics and Astronautics'), ('17', 'Political Science'), ('18', 'Mathematics'), ('20', 'Biological Engineering'), ('21', 'Humanities'), ('22', 'Nuclear Science and Engineering'), ('24', 'Linguistics and Philosophy')]
hard = [('1', 'Civil and Environmental Engineering'), ('2', 'Mechanical Engineering'), ('2-OE', 'Mechanical and Ocean Engineering'), ('3', 'Materials Science and Engineering'), ('3-A', 'Materials Science and Engineering'), ('3-C', 'Archaeology and Materials'), ('4', 'Architecture'), ('5', 'Chemistry'), ('5-7', 'Chemistry and Biology'), ('6', 'Electrical Engineering and Computer Science'), ('6-1', 'Electrical Science and Engineering'), ('6-14', 'Computer Science, Economics, and Data Science'), ('6-2', 'Electrical Engineering and Computer Science'), ('6-3', 'Computer Science and Engineering'), ('6-4', 'Artificial Intelligence and Decision Making'), ('6-7', 'Computer Science and Molecular Biology'), ('6-9', 'Computation and Cognition'), ('7', 'Biology'), ('8', 'Physics'), ('9', 'Brain and Cognitive Sciences'), ('CMS', 'Comparative Media Studies'), ('STS', 'Science, Technology, and Society/Second Major'), ('10', 'Chemical Engineering'), ('10', 'Chemical Engineering'), ('10-B', 'Chemical-Biological Engineering'), ('11', 'Urban Studies and Planning'), ('11-6', 'Urban Science and Planning with Computer Science'), ('12', 'Earth, Atmospheric, and Planetary Sciences'), ('14', 'Economics'), ('14-1', 'Economics'), ('14-2', 'Mathematical Economics'), ('15', 'Management'), ('15-1', 'Management'), ('15-2', 'Business Analytics'), ('15-3', 'Finance'), ('16', 'Aeronautics and Astronautics'), ('17', 'Political Science'), ('17', 'Political Science'), ('18', 'Mathematics'), ('18-C', 'Mathematics with Computer Science'), ('20', 'Biological Engineering'), ('21', 'Humanities'), ('21A', 'Anthropology'), ('21E', 'Humanities and Engineering'), ('21G', 'Global Studies and Languages'), ('21H', 'History'), ('21L', 'Literature'), ('21M-1', 'Music'), ('21M-2', 'Theater Arts'), ('21S', 'Humanities and Science'), ('21W', 'Writing'), ('22', 'Nuclear Science and Engineering'), ('24', 'Linguistics and Philosophy'), ('24-1', 'Philosophy'), ('24-2', 'Linguistics and Philosophy')]

endit = ''
seq = 0
sequential = True
print()
print('<Enter> to continue')
print('q to quit')
print('e/h for easy/hard')
print('s/r for sequential/random')
print()
result = easy

while endit != 'q':
  seq %= len(result)
  index = 0
  if sequential:
    index = seq
  else:
    index = int(random.random()*len(result))
  endit = input(str(result[index][0])+' ')
  print(result[index][1])
  seq += 1
  if endit == 's':
    sequential = True
  if endit == 'r':
    sequential = False
  if endit == 'e':
    if sequential:
      seq = 0
    result = easy
  if endit == 'h':
    if sequential:
      seq = 0
    result = hard
  print()
print('Quitted.')
