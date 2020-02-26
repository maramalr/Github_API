import unittest
from unittest import mock
from repo_api import get_repo 
import json
import requests


class test_get_repo(unittest.TestCase):
    @mock.patch('repo_api.get_repo')
    
    def test_get_repo(self, mockedReq):
    
        mockedReq.return_value = [['Repo: 567_Testing Number of commits: 2 '],['Repo: Animal-Card Number of commits: 2 '], 
                                  ['Repo: Assignment0 Number of commits: 1 '], ['Repo: frontend-nanodegree-arcade-game Number of commits: 30 '],
                                  ['Repo: frontend-nanodegree-feedreader Number of commits: 26 '], ['Repo: frontend-nanodegree-mobile-portfolio Number of commits: 30 '],
                                  ['Repo: frontend-nanodegree-resume Number of commits: 30 '], ['Repo: gedcom-analyzer Number of commits: 9 '], ['Repo: Github_API Number of commits: 13 '],
                                  ['Repo: markup Number of commits: 7 '], ['Repo: Neighbourhood-project Number of commits: 21 '],
                                  ['Repo: PlanPackRepeat Number of commits: 30 '], ['Repo: Portfolio- Number of commits: 2 '], 
                                  ['Repo: SWW810Homeworks Number of commits: 4 '], ['Repo: Triangle567 Number of commits: 12 ']]

        expected = [['Repo: 567_Testing Number of commits: 2 '],['Repo: Animal-Card Number of commits: 2 '], 
                    ['Repo: Assignment0 Number of commits: 1 '], ['Repo: frontend-nanodegree-arcade-game Number of commits: 30 '],
                    ['Repo: frontend-nanodegree-feedreader Number of commits: 26 '], ['Repo: frontend-nanodegree-mobile-portfolio Number of commits: 30 '],
                    ['Repo: frontend-nanodegree-resume Number of commits: 30 '], ['Repo: gedcom-analyzer Number of commits: 9 '], ['Repo: Github_API Number of commits: 13 '],
                    ['Repo: markup Number of commits: 7 '], ['Repo: Neighbourhood-project Number of commits: 21 '],
                    ['Repo: PlanPackRepeat Number of commits: 30 '], ['Repo: Portfolio- Number of commits: 2 '], 
                    ['Repo: SWW810Homeworks Number of commits: 4 '], ['Repo: Triangle567 Number of commits: 12 ']]
                    
        github_id = 'maramalr'
        self.assertEqual(get_repo(github_id), expected)

        
if __name__ == '__main__':
    unittest.main()