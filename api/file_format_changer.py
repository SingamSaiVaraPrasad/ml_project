import tensorflow as tf

# Load the model
model = tf.keras.models.load_model(r"D:\vs code files new\2024\project\h5format\model.h5", compile=False)

# Check if the model has a loss function set
if model.loss:
    # Remove the 'fn' argument from the loss configuration
    loss_config = model.loss.get_config()
    loss_config.pop('fn', None)
    new_loss = tf.keras.losses.SparseCategoricalCrossentropy(**loss_config)
else:
    # Set a new loss function if the model was loaded without one
    new_loss = tf.keras.losses.SparseCategoricalCrossentropy()

# Recompile the model with the new loss
model.compile( loss=new_loss, metrics=model.metrics)

# Save the model again
model.save(r"D:\vs code files new\2024\project\h5format\model_fixed.h5")
