function [error_train, error_val] = ungradedRandomPlotting(X, y, Xval, yval, lambda)

% we'll check the cross validation set against the training set, hence the training set size is all what we need

m = size(X, 1);

	% vectors for storing traing errors and cross validation errors
	error_train = zeros(m,1);
	error_val =  zeros(m,1);
	% the lambda
	lambda = 0.01;
	% number of times to loop for picking random values
	loops = 50;

	% pick a random value "loops" times, summarise the calculated the errors, to below doing an average
	for l=1:loops

		% Concretely, to determine the training error and cross validation error for
		% i examples, (:1a:) you should first randomly select i examples from the training set
		% (:1b:) and i examples from the cross validation set. (:2:) You will then learn the param-
		% eters theta using the randomly chosen training set and (:3a:) evaluate the parameters
		% theta on the randomly chosen training set (:3b:) and cross validation set.

		% i = number of training examples
		for i=1:m
			% ---
			% test set
			% ---

			% (:1a:) randomly select i rows
			sel = randperm(size(X, 1));
			sel = sel(1:i);

			% create a matrix consisting only of the randomly selected rows from X and y
			X_sel = X(sel,:);
			y_sel = y(sel,:);

			% (:2:) learn parameters theta using the randomly chose training set
			theta = trainLinearReg(X_sel, y_sel, lambda);
	
			% (:3a:) evaluate the parameters theta on the randomly chosen training set
			[J, grad] = linearRegCostFunction(X_sel, y_sel, theta, 0);

			% accumulate errors for i-training examples
			error_train(i) = error_train(i) + J;

			% ---
			% cross validation set
			% ---
			% (:1b:) ... and i examples from the cross validation set
			sel = randperm(size(Xval, 1));
			sel = sel(1:i);
			X_sel = Xval(sel,:);
			y_sel = yval(sel,:);
			% (:3b:) ... and cross validation set
			[J, grad_val] = linearRegCostFunction(X_sel, y_sel, theta, 0);

			error_val(i) = error_val(i) + J;

		end
	end

	% finding the average
	error_train = error_train ./ loops;
	error_val = error_val ./ loops;

	% least but not last, do some plotting to visualise our results
	%plot(1:m, error_train, 1:m, error_val);
	%xlabel('Number of training examples');
	%ylabel('Error');
	%axis([0 13 0 100]);
	%legend('Train', 'Cross Validation');






