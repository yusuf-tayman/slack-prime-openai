# slack-prime-openai

This project integrates Slack with the OpenAI API to allow users to ask questions and receive answers from the OpenAI GPT-3 language model.

## Requirements
To use this project, you will need to install the following dependencies:

[slack_bolt](https://pypi.org/project/slack-bolt)

[openai](https://pypi.org/project/openai)

You can install these dependencies using pip:

```bash
pip install slack_bolt openai
```

## Usage

* Set up a Slack bot and obtain the bot's API token.
* Set up an OpenAI API key.
* Set the SLACK_BOT_TOKEN and OPENAI_API_KEY environment variables with the values of your bot's API token and OpenAI API key, respectively.
* Run the main.py file to start the bot.
* In a Slack channel, mention the bot and ask it any question. The bot will use OpenAI's GPT-3 model to generate an answer.

* Note: The bot will only respond to messages that specifically mention it.

## Example:

```
User: @my-bot write unit test with spring and code examples
```

```
Bot: Spring makes unit testing easy by providing a testing framework and test libraries. Below is an example of how to write a basic unit test using the Spring framework and JUnit 5.
First, create a class for the unit test:
java
@ExtendWith(SpringExtension.class)
@ContextConfiguration(classes = {MyClassToTest.class})
public class MyClassToTestTest { 

    @Autowired
    private MyClassToTest classToTest;

    @Test
    public void testMyFunction() {
        int result = classToTest.myFunction(1, 2);
        assertEquals(3, result);
    }
}
Next, create a configuration class which sets up any mocks or dependencies that may be needed for the unit test:
java
@Configuration
public class TestConfiguration {

    @Bean
    public MyClassToTest myClassToTest() {
        // Create and return a new instance of MyClassToTest
        return new MyClassToTest();
    }

}
Finally, create the class under test:
java
public class MyClassToTest {
    
    public int myFunction(int a, int b) {
        // Some logic here...
        return a + b;
    }

}
When the above code is executed, the unit test will assert that the result of MyFunction() is equal to 3 when given parameters of 1 and 2.
```
