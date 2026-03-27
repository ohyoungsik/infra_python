# Step17_file4.py

import os
import re


if __name__ == "__main__" :
  file_path=os.path.join(os.getcwd(),'config.text')
  # 문자열 한줄 한줄을 저장할 empty list
  updated_lines=[]
  
  # SELINUX=xxxx pattern 의 문자열을 찾을 정규 표현식
  pattern=r"^SELINUX=[a-zA-Z]+"
  
  with open(file_path,'r',encoding='utf-8') as f:
      for line in f:
        # 만일 pattern 에 매칭되는 line 이면
        if(re.match(pattern,line)):
            # SELINUX=xxx 를 SELINUX=disabled 로 치환(substitution)하기
            result = re.sub(pattern,"SELINUX=disabled",line)
            updated_lines.append(result)
        else:
          updated_lines.append(line)
    

    
  with open(file_path,'w',encoding='utf-8') as f:
      f.writelines(updated_lines)
      
print('config.text. 파일을 수정했습니다.')
        