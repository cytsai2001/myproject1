movielist=input('Type names and ratings or movies: (separated by comma)')
newlist=movielist.split(',')
namelist=newlist[0:-1:2]
ratinglist=newlist[1:-1:2]
ratinglist.extend(list((newlist[-1])))
newratinglist=list(float(x) for x in ratinglist)
#finaldict= dict(zip(namelist,newratinglist))
#sort_rating = sorted(finaldict.keys())
print(namelist)
print(newratinglist)
