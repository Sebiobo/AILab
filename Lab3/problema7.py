preturi=[100,None,50,None,None,25,34,54]

preturi_curate=list(filter(lambda preturi:preturi is not None,preturi))

preturi_reduse=list(map(lambda preturi_curate:preturi_curate * 0.9,preturi_curate))

print(preturi_curate)
print(preturi_reduse)