$(document).ready(function() {
    $('#create-rule-form').submit(function(event) {
        event.preventDefault();
        const ruleString = $('#rule').val();

        $.ajax({
            type: 'POST',
            url: '/create_rule',
            contentType: 'application/json',
            data: JSON.stringify({ rule_string: ruleString }),
            success: function(response) {
                if (response.status === 'success') {
                    alert('Rule created successfully');
                    console.log(response.ast);
                    $('#ast').val(JSON.stringify(response.ast, null, 2));
                } else {
                    alert('Error: ' + response.message);
                }
            },
            error: function(error) {
                alert('Error creating rule: ' + error.responseJSON.message);
                console.log(error);
            }
        });
    });

    $('#evaluate-rule-form').submit(function(event) {
        event.preventDefault();
        const ast = $('#ast').val();
        const data = $('#data').val();

        try {
            const parsedAST = JSON.parse(ast);
            const parsedData = JSON.parse(data);

            $.ajax({
                type: 'POST',
                url: '/evaluate_rule',
                contentType: 'application/json',
                data: JSON.stringify({ ast: parsedAST, data: parsedData }),
                success: function(response) {
                    if (response.status === 'success') {
                        $('#result').text('Result: ' + response.result);
                        if (response.result) {
                            $('#result').removeClass('result-false').addClass('result-true');
                        } else {
                            $('#result').removeClass('result-true').addClass('result-false');
                        }
                    } else {
                        alert('Error: ' + response.message);
                    }
                },
                error: function(error) {
                    alert('Error evaluating rule: ' + error.responseJSON.message);
                    console.log(error);
                }
            });
        } catch (e) {
            alert('Invalid JSON format in AST or Data.');
        }
    });
});
