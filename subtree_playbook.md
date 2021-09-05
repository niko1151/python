# Funcing uoverskuligt med subtrees, men hvad ellers?

## Add

    % git subtree add -P mooc/data_analysis_with_python_summer_2021 git@github.com:csmastersUH/data_analysis_with_python_summer_2021.git main
  
og 
  
    % git subtree -d add -P elev_python_og_dataanalyse git@github.com:TEC-Prog-Stud/Python-og-DataAnalyse.git main


## pull
    
    % git subtree -d pull -P elev_python_og_dataanalyse git@github.com:TEC-Prog-Stud/Python-og-DataAnalyse.git main
 
medfører:

    command: {pull}
    quiet: {}
    revs: {}
    dir: {elev_python_og_dataanalyse}
    opts: {git@github.com:TEC-Prog-Stud/Python-og-DataAnalyse.git main}

    From github.com:TEC-Prog-Stud/Python-og-DataAnalyse
     * branch            main       -> FETCH_HEAD
    Already up to date.
    
Man kan droppe `-d` for at få et mere simpelt svar:

    % git subtree pull -P elev_python_og_dataanalyse git@github.com:TEC-Prog-Stud/Python-og-DataAnalyse.git main 
    From github.com:TEC-Prog-Stud/Python-og-DataAnalyse
     * branch            main       -> FETCH_HEAD
    Already up to date.


## push

## remove

    % git rm -rf mooc/data_analysis_with_python_summer_2021 
  
Lidt tvivlsomt, for kommandoen fjerne filerne... men også subtree prefix? Tjo, måske nok...
  
