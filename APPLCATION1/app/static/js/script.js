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

        $.ajax({
            type: 'POST',
            url: '/evaluate_rule',
            contentType: 'application/json',
            data: JSON.stringify({ ast: JSON.parse(ast), data: JSON.parse(data) }),
            success: function(response) {
                if (response.status === 'success') {
                    $('#result').text('Result: ' + response.result);
                } else {
                    alert('Error: ' + response.message);
                }
            },
            error: function(error) {
                alert('Error evaluating rule: ' + error.responseJSON.message);
                console.log(error);
            }
        });
    });
});
