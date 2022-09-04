# AWS CLI

- _**Upload files to S3 bucket**_ :

    SYNTAX : 
    ```
    aws s3 cp <file-path> <bucket-name> (or)
    aws s3 mv <file-path> <bucket-name>
    ```

    EXAMPLE :
    ```
    aws s3 cp test.txt priya-demobucket
    aws s3 mv test.txt priya-demobucket
    ```

- _**Download object from S3 bucket**_ 

    SYNTAX : 
    ```
    aws s3 cp <bucket-name/object> <file-path> 
    ```

    EXAMPLE :
    ```
    aws s3 cp priya-demobucket/test.txt hello.txt
    ```
- _**List all objects in S3 bucket**_

    SYNTAX : 
    ```
    aws s3 ls <bucket-name>
    ```

    EXAMPLE :
    ```
    aws s3 ls priya-demobucket
    ```

- _**Delete an object from S3 bucket**_

    SYNTAX : 
    ```
    aws s3 rm <bucket-name/object>
    ```

    EXAMPLE :
    ```
    aws s3 rm priya-demobucket/test.txt
    ```

# Reference

[AWS CLI Commands - Docs](https://docs.aws.amazon.com/cli/latest/userguide/cli-services-s3-commands.html)

[boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html)

[AWS SDK examples - Github](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/python/example_code/s3/s3_basics/object_wrapper.py)

[Upload, download and delete files in S3 using python](https://www.datacourses.com/how-to-upload-download-and-delete-files-on-s3-server-in-python-3111/)

[Argparse - Python Documentation](https://docs.python.org/3/library/argparse.html)