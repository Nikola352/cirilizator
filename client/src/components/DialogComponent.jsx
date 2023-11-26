import {
    Button,
    Dialog,
    DialogHeader,
    DialogBody,
    DialogFooter,
  } from "@material-tailwind/react";
export default function DialogComponent({open, handleSubmit, text, error}) {
  return (
    <div>
      {/* DIALOG */}
      <Dialog open={open} handler={handleSubmit} className='w-11/12 xl:w-1/2 mt-80 h-64 shadow-xl rounded-3xl py-4 px-8'>
                    <DialogHeader className="mt-5 mb-4 text-2xl">{error ? "Грешка!": "Честитамо!"}</DialogHeader>
                    <DialogBody className="mt-4 text-lg">
                    {text}
                    </DialogBody>
                    <DialogFooter>
                    <Button
                        variant="text"
                        color="red"
                        onClick={handleSubmit}
                        className="pb-4"
                    >
                        <span className="text-primary">Затвори</span>
                    </Button>
                    <Button  onClick={handleSubmit}>
                        <span className="text-xl">Потврди</span>
                    </Button>
                    </DialogFooter>
                </Dialog>
    </div>
  );
}