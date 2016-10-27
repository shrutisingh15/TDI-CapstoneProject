from flask import Flask, render_template, request, redirect, url_for




app = Flask(__name__)
@app.route('/')
def main():
  return render_template('index1.html')

@app.route('/clustermap')
def com():
  return render_template('temp.html') 

@app.route('/explore')
def ind():
  return render_template('ind.html')

@app.route('/comparison')
def violin():
  return render_template('violin1.html')

@app.route('/kmeanscode')
def kcod():
    return render_template('Website_Code.html')  

@app.route('/regressioncode')
def rcod():
    return render_template('Countries_Regression.html')  

  
''' 


@app.route('/graph', methods=['GET'])
def graph():
	#Data into Pandas
	
	Input = pd.read_csv('Input.csv')
	Input=Input.set_index(keys='Country Name')
	X = np.array(Input)
    kmeans = KMeans(n_clusters=7,max_iter=300,n_init=10).fit(X)
    labels = kmeans.labels_
    labels_true = Input.index
    cluster_centers_indices = kmeans.cluster_centers_
    n_clusters_= len(cluster_centers_indices)
	
	p =figure(figsize = [10,8])

    colors=cycle('bgrcmykbgrcmykbgrcmykbgrcmyk')
    for k, col in zip(range(n_clusters_), colors):
         class_members = labels == k
         p.plot(X[class_members, 0], X[class_members, 1], col + '.',markersize=12)

		 

    legend_labels=set(labels)
    p.title('Estimated number of clusters: %d' %(n_clusters_), fontsize=14) 
    p.xlabel(Input.columns[0],fontsize=14)
    p.ylabel(Input.columns[1],fontsize=14)
    p.legend(legend_labels, loc='best')
    
    script, div = components(p)
	

	return render_template('graph.html', script=script, div=div)
    '''
	
	
@app.errorhandler(404)
def page_not_found(error):
    return 'Sorry, page not found', 404




if __name__ == '__main__':
  app.run(port=33507)
