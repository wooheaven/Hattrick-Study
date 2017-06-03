# How to use python3 with jupyternotebook
```{bash}
$ conda info --envs
# conda environments:
#
python2.7                /usr/local/anaconda/anaconda2/envs/python2.7
python3                  /usr/local/anaconda/anaconda2/envs/python3
root                  *  /usr/local/anaconda/anaconda2

$ source activate python3

$ conda info --envs
# conda environments:
#
python2.7                /usr/local/anaconda/anaconda2/envs/python2.7
python3               *  /usr/local/anaconda/anaconda2/envs/python3
root                     /usr/local/anaconda/anaconda2

(python3) $ jupyter notebook --notebook-dir=`pwd` --no-browser --ip=0.0.0.0
[I 04:53:39.381 NotebookApp] Writing notebook server cookie secret to /run/user/1000/jupyter/notebook_cookie_secret
[I 04:53:42.468 NotebookApp] Serving notebooks from local directory: /home/rwoo/02_workspace/08_Hattrick_Workspace/Hattrick-Study
[I 04:53:42.468 NotebookApp] 0 active kernels 
[I 04:53:42.468 NotebookApp] The Jupyter Notebook is running at: http://0.0.0.0:8888/?token=24709032c20da6463d2014bbb2a998a019ec66e1ea4723be
[I 04:53:42.469 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[C 04:53:42.469 NotebookApp] 

    Copy/paste this URL into your browser when you connect for the first time,
    to login with a token:
        http://0.0.0.0:8888/?token=24709032c20da6463d2014bbb2a998a019ec66e1ea4723be

^C[I 06:10:17.844 NotebookApp] interrupted
Serving notebooks from local directory: /home/rwoo/02_workspace/08_Hattrick_Workspace/Hattrick-Study
0 active kernels 
The Jupyter Notebook is running at: http://0.0.0.0:8888/?token=24709032c20da6463d2014bbb2a998a019ec66e1ea4723be
Shutdown this notebook server (y/[n])? y
[C 06:10:19.539 NotebookApp] Shutdown confirmed
[I 06:10:19.539 NotebookApp] Shutting down kernels

(python3) $ source deactivate python3

$ conda info --envs
# conda environments:
#
python2.7                /usr/local/anaconda/anaconda2/envs/python2.7
python3                  /usr/local/anaconda/anaconda2/envs/python3
root                  *  /usr/local/anaconda/anaconda2
```
